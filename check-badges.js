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

// Helper function to read JSON file and return parsed data
function readBadgesFile() {
    if (!fs.existsSync(badgesPath)) {
        console.error('Error: badges.json not found.');
        process.exit(1);
    }
    return JSON.parse(fs.readFileSync(badgesPath, 'utf8'));
}

// Helper function to write only changed lines back to the file
function writeUpdatedBadges(originalBadges, updatedBadges) {
    const updatedLines = [];
    let changesMade = false;

    originalBadges.plugins.forEach((originalPlugin, index) => {
        const updatedPlugin = updatedBadges.plugins[index];

        // Compare each plugin's relevant fields
        if (
            originalPlugin.latestReleaseUrl !== updatedPlugin.latestReleaseUrl ||
            originalPlugin.releaseDate !== updatedPlugin.releaseDate
        ) {
            changesMade = true;
            updatedLines.push(JSON.stringify(updatedPlugin, null, 4));
        } else {
            updatedLines.push(JSON.stringify(originalPlugin, null, 4));
        }
    });

    if (changesMade) {
        fs.writeFileSync(badgesPath, `{\n  "plugins": [\n${updatedLines.join(',\n')}\n  ]\n}\n`);
        console.log('Updated only the necessary lines in badges.json.');
    } else {
        console.log('No updates found for badges.json.');
    }
}

async function checkAndUpdateBadges() {
    const originalBadges = readBadgesFile();
    const updatedBadges = JSON.parse(JSON.stringify(originalBadges)); // Deep clone for modification

    for (const plugin of updatedBadges.plugins) {
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

            // Update the plugin fields if changes are detected
            if (plugin.latestReleaseUrl !== newReleaseUrl || plugin.releaseDate !== releaseDate) {
                plugin.latestReleaseUrl = newReleaseUrl;
                plugin.releaseDate = releaseDate;
            }
        } catch (error) {
            if (error.response && error.response.status === 404) {
                console.warn(`No releases found for ${plugin.name}.`);
                if (plugin.latestReleaseUrl !== "") {
                    plugin.latestReleaseUrl = "";
                }
            } else {
                console.error(`Error fetching release for ${plugin.name}: ${error.message}`);
            }
        }
    }

    // Update totalPlugins count (only count plugins, not dev tools)
    updatedBadges.totalPlugins.message = updatedBadges.plugins.length.toString();

    // Write only the necessary changes back to the file
    writeUpdatedBadges(originalBadges, updatedBadges);
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
