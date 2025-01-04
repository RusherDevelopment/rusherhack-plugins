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

async function checkAndUpdateBadges() {
    if (!fs.existsSync(badgesPath)) {
        console.error('Error: badges.json not found.');
        process.exit(1);
    }

    let badges = JSON.parse(fs.readFileSync(badgesPath, 'utf8'));
    let updated = false;

    for (const plugin of badges.plugins) {
        if (plugin.latestReleaseUrl === "null") continue;

        const repoUrl = plugin.url.replace('https://github.com/', '');
        const apiUrl = `https://api.github.com/repos/${repoUrl}/releases/latest`;

        try {
            const response = await axiosInstance.get(apiUrl);
            const latestRelease = response.data;
            const jarFiles = latestRelease.assets.filter(asset => asset.name.endsWith('.jar'));

            let newReleaseUrl = null;

            if (jarFiles.length === 1) {
                newReleaseUrl = jarFiles[0].browser_download_url;
            } else if (jarFiles.length > 1) {
                newReleaseUrl = latestRelease.html_url;
            }

            // Only update if there's a real change in the release URL
            if (plugin.latestReleaseUrl !== newReleaseUrl) {
                console.log(`Updating ${plugin.name}: ${plugin.latestReleaseUrl} -> ${newReleaseUrl}`);
                plugin.latestReleaseUrl = newReleaseUrl;
                updated = true;
            } else {
                console.log(`No update needed for ${plugin.name}.`);
            }
        } catch (error) {
            if (error.response && error.response.status === 404) {
                console.warn(`No releases found for ${plugin.name}.`);
                if (plugin.latestReleaseUrl !== "null") {
                    plugin.latestReleaseUrl = "null";
                    updated = true;
                }
            } else {
                console.error(`Error fetching release for ${plugin.name}: ${error.message}`);
            }
        }
    }

    if (updated) {
        fs.writeFileSync(badgesPath, JSON.stringify(badges, null, 4)); // Keep consistent formatting
        console.log('Updated badges.json.');
    } else {
        console.log('No updates found for badges.json.');
    }
}

checkAndUpdateBadges().then(() => {
    console.log('Badge check complete.');
});
