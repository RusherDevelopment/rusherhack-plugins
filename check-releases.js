const fs = require('fs');
const axios = require('axios');

const GH_TOKEN = process.env.GITHUB_TOKEN;
const axiosInstance = axios.create({
    headers: {
        Authorization: `token ${GH_TOKEN}`,
        Accept: 'application/vnd.github.v3+json'
    }
});

const badgesPath = './badges.json';
const readmePath = './README.md';

let badges = JSON.parse(fs.readFileSync(badgesPath, 'utf8'));

async function checkAndUpdateReleases() {
    let updated = false;

    for (const plugin of badges.plugins) {
        if (plugin.latestReleaseUrl === "null") continue; // Skip plugins with no releases

        const repoUrl = plugin.url.replace('https://github.com/', '');
        const apiUrl = `https://api.github.com/repos/${repoUrl}/releases/latest`;

        try {
            const response = await axiosInstance.get(apiUrl);
            const latestRelease = response.data;
            const jarFiles = latestRelease.assets.filter(asset => asset.name.endsWith('.jar'));

            let newReleaseUrl = null;

            if (jarFiles.length === 1) {
                newReleaseUrl = jarFiles[0].browser_download_url; // Single .jar file
            } else if (jarFiles.length > 1) {
                newReleaseUrl = latestRelease.html_url; // Multiple files, use tag URL
            }

            if (plugin.latestReleaseUrl !== newReleaseUrl) {
                console.log(`Updating ${plugin.name}: ${plugin.latestReleaseUrl} -> ${newReleaseUrl}`);
                plugin.latestReleaseUrl = newReleaseUrl;
                updated = true;
            }
        } catch (error) {
            if (error.response && error.response.status === 404) {
                console.warn(`No releases found for ${plugin.name}.`);
                plugin.latestReleaseUrl = "null";
                updated = true;
            } else {
                console.error(`Error fetching release for ${plugin.name}: ${error.message}`);
            }
        }
    }

    if (updated) {
        fs.writeFileSync(badgesPath, JSON.stringify(badges, null, 4));
        console.log('Updated badges.json.');

        updateReadme();
    } else {
        console.log('No updates found.');
    }
}

function updateReadme() {
    let readmeContent = fs.readFileSync(readmePath, 'utf8');

    badges.plugins.forEach((plugin) => {
        const badgeRegex = new RegExp(`\\\!\GitHub Downloads \all releases\\\[^\]+\\\[^\]+\`, 'g');
        const newBadge = `[![GitHub Downloads (all releases)](${plugin.latestReleaseUrl})](${plugin.latestReleaseUrl})`;
        readmeContent = readmeContent.replace(badgeRegex, newBadge);
        console.log(`Updated badge for ${plugin.name} in README.md.`);
    });

    fs.writeFileSync(readmePath, readmeContent);
    console.log('Updated README.md.');
}

checkAndUpdateReleases().then(() => {
    console.log('Release check complete.');
});