const fs = require('fs');

// Load parsed badges and README
const parsedBadges = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
let readmeContent = fs.readFileSync('README.md', 'utf8');

// Regex to match the plugins list section in the README
const sectionRegex = /<!-- START PLUGINS LIST -->\n([\s\S]*?)\n<!-- END PLUGINS LIST -->/;

// Extract existing plugins list section
const sectionMatch = sectionRegex.exec(readmeContent);
if (!sectionMatch) {
  console.error('Error: Could not find the plugins list section in the README.');
  process.exit(1);
}

let pluginsListContent = sectionMatch[1].trim();

// Regex to match individual plugins in the extracted section
const pluginRegex = /- ### (.*?).*?\s*<br>\n\n\s*!GitHub Downloads all releases(.*?)(.*?)/g;

// Map to hold parsed plugin entries from the extracted section
const readmePlugins = new Map();
let match;

// Parse the plugins list to extract plugin names and their download URLs
while ((match = pluginRegex.exec(pluginsListContent)) !== null) {
  const pluginName = match[1].trim();
  const badgeUrl = match[2].trim();
  const downloadUrl = match[3].trim();
  readmePlugins.set(pluginName, { badgeUrl, downloadUrl });
}

// Flag to track if changes are made
let changesMade = false;

// Check and update each plugin in parsed badges
parsedBadges.forEach(({ name, repo, latestReleaseUrl }) => {
  if (readmePlugins.has(name)) {
    const { badgeUrl, downloadUrl } = readmePlugins.get(name);

    // Construct expected badge URL
    const expectedBadgeUrl = `https://img.shields.io/github/downloads/${repo}/total`;

    // Check if the download URL needs updating
    if (downloadUrl !== latestReleaseUrl) {
      console.log(`Updating download URL for ${name}`);
      pluginsListContent = pluginsListContent.replace(downloadUrl, latestReleaseUrl);
      changesMade = true;
    }

    // Check if the badge URL needs updating
    if (badgeUrl !== expectedBadgeUrl) {
      console.log(`Updating badge URL for ${name}`);
      pluginsListContent = pluginsListContent.replace(badgeUrl, expectedBadgeUrl);
      changesMade = true;
    }
  } else {
    console.log(`No matching plugin found in README for ${name}`);
  }
});

// Write updated plugins list back into the README if changes were made
if (changesMade) {
  readmeContent = readmeContent.replace(
    sectionRegex,
    `<!-- START PLUGINS LIST -->\n${pluginsListContent}\n<!-- END PLUGINS LIST -->`
  );
  fs.writeFileSync('README.md', readmeContent, 'utf8');
  console.log('README updated successfully.');
  process.exit(0); // Indicate success
} else {
  console.log('No changes made to README.');
  process.exit(1); // Indicate no changes
}
