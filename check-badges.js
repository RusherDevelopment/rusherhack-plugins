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

// Function to sort keys in an object to maintain consistent order
function sortKeys(obj) {
    return Object.keys(obj).sort().reduce((sorted, key) => {
        sorted[key] = obj[key];
        return sorted;
    }, {});
}

async function checkAndUpdateBadges() {
    if (!fs.existsSync(badgesPath)) {
        console.error('Error: badges.json not found.');
        process.exit(1);
    }

    let badges = JSON.parse(fs.readFileSync(badgesPath, 'utf8'));
    let originalBadges = JSON.parse(JSON.stringify(badges)); // Deep clone for comparison
    let updated = false;

    for (const plugin of badges.plugins) {
        if (!plugin.latestReleaseUrl) continue; // Skip if latestReleaseUrl is missing or empty

        const repoUrl = plugin.url.replace('https://github.com/', '');
        const apiUrl = `https://api.github.com/repos/${repoUrl}/releases/latest`;

        try {
            const response = await axiosInstance.get(apiUrl);
            const latestRelease = response.data;
            const jarFiles = latestRelease.assets.filter(asset => asset.name.endsWith('.jar'));

            let newReleaseUrl = "";
            if (jarFiles.length === 1) {
                newReleaseUrl = jarFiles[0].browser_download_url;
            } else if (jarFiles.length > 1) {
                newReleaseUrl = latestRelease.html_url;
            }

            const releaseDate = new Date(latestRelease.published_at).toISOString().split('T')[0];

            console.log(`Found release URL for ${plugin.name}: ${newReleaseUrl}`);
            console.log(`Found release date for ${plugin.name}: ${releaseDate}`);

            // Check for changes before updating
            if (plugin.latestReleaseUrl !== newReleaseUrl || plugin.releaseDate !== releaseDate) {
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

    // Sort keys in each plugin to maintain consistent formatting
    badges.plugins = badges.plugins.map(sortKeys);

    // Compare with the original file to decide whether to write changes
    if (!deepEqual(badges, originalBadges)) {
        fs.writeFileSync(badgesPath, JSON.stringify(badges, null, 4) + '\n'); // Ensure newline at EOF
        console.log('Updated badges.json.');
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
