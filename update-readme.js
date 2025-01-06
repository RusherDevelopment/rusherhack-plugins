const fs = require('fs');

// Load README
let readmeContent = fs.readFileSync('README.md', 'utf8');

// Regex to match the plugins list section in the README
const sectionRegex = /<!-- START PLUGINS LIST -->([\s\S]*?)<!-- END PLUGINS LIST -->/;
const sectionMatch = sectionRegex.exec(readmeContent);

if (!sectionMatch) {
  console.error('Error: Could not find the plugins list section in the README.');
  process.exit(1);
}

const pluginsListContent = sectionMatch[1].trim();

// Regex to match individual plugin entries and their download URLs
const pluginRegex = /- ### (.+?).*?!GitHub Downloads all releases(https:\/\/img\.shields\.io\/github\/downloads\/.+?\/total)(.+?)/g;
const readmePlugins = new Map();
let match;

// Extract plugin names and URLs from README
while ((match = pluginRegex.exec(pluginsListContent)) !== null) {
  const pluginName = match[1].trim();
  const currentBadgeUrl = match[2].trim();
  const currentDownloadUrl = match[3].trim();
  readmePlugins.set(pluginName.toLowerCase(), { pluginName, currentBadgeUrl, currentDownloadUrl });
}

// Log parsed plugin names from README
console.log('Parsed plugin names from README:', Array.from(readmePlugins.keys()));

if (readmePlugins.size === 0) {
  console.error('No plugins were found. Please check the README format.');
  process.exit(1);
}

// Load parsed badges
const parsedBadges = JSON.parse(fs.readFileSync(process.argv[2], 'utf8')).plugins;

// Flag to track changes
let changesMade = false;

// Iterate over parsed badges to find matching plugins in the README
parsedBadges.forEach(({ name, latestReleaseUrl }) => {
  const normalizedPluginName = name.toLowerCase();
  const pluginEntry = readmePlugins.get(normalizedPluginName);

  if (pluginEntry) {
    console.log(`Matching plugin found in README for ${name}`);
    const expectedBadgeUrl = `https://img.shields.io/github/downloads/${name}/total`;

    // Check if URLs need updating
    if (pluginEntry.currentDownloadUrl !== latestReleaseUrl) {
      console.log(`Updating download URL for ${name}`);
      const newBadge = `[![GitHub Downloads (all releases)](${expectedBadgeUrl})](${latestReleaseUrl})`;

      // Update the plugin entry in the README
      const oldEntry = `- ### [${pluginEntry.pluginName}] [![GitHub Downloads (all releases)](${pluginEntry.currentBadgeUrl})](${pluginEntry.currentDownloadUrl})`;
      const newEntry = `- ### [${pluginEntry.pluginName}] ${newBadge}`;

      readmeContent = readmeContent.replace(oldEntry, newEntry);
      changesMade = true;
    }
  } else {
    console.log(`No matching plugin found in README for ${name}`);
  }
});

// Write updated README if changes were made
if (changesMade) {
  console.log('Changes detected, updating README...');
  fs.writeFileSync('README.md', readmeContent, 'utf8');
  console.log('README updated successfully.');
} else {
  console.log('No changes made to README.');
}
