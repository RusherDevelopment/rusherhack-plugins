const fs = require('fs');
const axios = require('axios');
const deepEqual = require('fast-deep-equal');

const GH_TOKEN = process.env.GITHUB_TOKEN;
const axiosInstance = axios.create({
    headers: {
        Authorization: `token ${GH_TOKEN}`,
        Accept: 'application/vnd.github.v3+json'
    }
});

const badgesPath = './badges.json';

async function checkAndUpdateBadges() {
    if (!fs.existsSync(badgesPath)) {
        console.error('Error: badges.json not found.');
        process.exit(1);
    }

    let badges = JSON.parse(fs.readFileSync(badgesPath, 'utf8'));
    let updated = false;

    for (const plugin of badges.plugins) {
        const repoUrl = plugin.url.replace('https://github.com/', '');
        const apiUrl = `https://api.github.com/repos/${repoUrl}/releases/latest`;

        try {
            const response = await axiosInstance.get(apiUrl);
            const latestRelease = response.data;
            const jarFiles = latestRelease.assets.filter(asset => asset.name.endsWith('.jar'));

            let newReleaseUrl = jarFiles.length === 1
                ? jarFiles[0].browser_download_url
                : jarFiles.length > 1
                ? latestRelease.html_url
                : "";

            const releaseDate = new Date(latestRelease.published_at).toISOString().split('T')[0];

            console.log(`Checking ${plugin.name}...`);
            console.log(`- Current URL: ${plugin.latestReleaseUrl}`);
            console.log(`- New URL: ${newReleaseUrl}`);
            console.log(`- Current Date: ${plugin.releaseDate}`);
            console.log(`- New Date: ${releaseDate}`);

            if (plugin.latestReleaseUrl !== newReleaseUrl || plugin.releaseDate !== releaseDate) {
                console.log(`- Updating ${plugin.name}`);
                plugin.latestReleaseUrl = newReleaseUrl;
                plugin.releaseDate = releaseDate;
                updated = true;
            }
        } catch (error) {
            if (error.response && error.response.status === 404) {
                console.warn(`No releases found for ${plugin.name}.`);
                if (plugin.latestReleaseUrl !== "") {
                    plugin.latestReleaseUrl = "";
                    updated = true;
                }
            } else {
                console.error(`Error fetching release for ${plugin.name}: ${error.message}`);
            }
        }
    }

    // Update totalPlugins count (only count plugins, not dev tools)
    badges.totalPlugins.message = badges.plugins.length.toString();

    if (updated) {
        fs.writeFileSync(badgesPath, JSON.stringify(badges, null, 4));
        console.log('Updated badges.json with minimal changes.');
    } else {
        console.log('No updates found for badges.json.');
    }
}

checkAndUpdateBadges()
    .then(() => {
        console.log('Badge check complete.');
        process.exit(0);
    })
    .catch(error => {
        console.error('Unexpected error:', error.message);
        process.exit(1);
    });
