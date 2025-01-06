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
console.log('Extracted plugins list content:\n', pluginsListContent);

// Regex to match individual plugin entries
const pluginRegex = /- ### ([^]+)/g;
const pluginNames = [];
let match;

// Extract plugin names from README
while ((match = pluginRegex.exec(pluginsListContent)) !== null) {
  pluginNames.push(match[1].trim());
}

// Log parsed plugin names from README
console.log('Parsed plugin names from README:', pluginNames);

if (pluginNames.length === 0) {
  console.error('No plugins were found. Please check the README format.');
  process.exit(1);
}

// Load parsed badges from badges.json
const parsedBadges = JSON.parse(fs.readFileSync(process.argv[2], 'utf8')).plugins;

// Map plugin names from the README for easier matching
const readmePlugins = new Map(pluginNames.map(name => [name.toLowerCase(), name]));

// Flag to track changes
let changesMade = false;

// Iterate over parsed badges to find matching plugins in the README
parsedBadges.forEach(({ name, latestReleaseUrl }) => {
  const normalizedPluginName = name.toLowerCase();
  console.log(`\nChecking plugin: ${name}`);
  console.log(`Latest release URL from badges.json: ${latestReleaseUrl}`);

  if (readmePlugins.has(normalizedPluginName)) {
    console.log(`Matching plugin found in README for ${name}`);

    // Regex to find the current download badge entry for this plugin
    const badgeRegex = new RegExp(
      `\!\GitHub Downloads \all releases\\\https://img\\.shields\\.io/github/downloads/${normalizedPluginName}/total\\\(.*?)\`,
      'g'
    );

    const match = badgeRegex.exec(readmeContent);
    if (match && match[1] !== latestReleaseUrl) {
      console.log(`Updating download URL for ${name}`);
      const updatedBadge = `[![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/${normalizedPluginName}/total)](${latestReleaseUrl})`;

      // Replace the old badge with the updated one
      readmeContent = readmeContent.replace(badgeRegex, updatedBadge);
      changesMade = true;
    } else {
      console.log(`No update needed for ${name}`);
    }
  } else {
    console.log(`No matching plugin found in README for ${name}`);
  }
});

// Write updated README if changes were made
if (changesMade) {
  console.log('\nChanges detected, updating README...');
  fs.writeFileSync('README.md', readmeContent, 'utf8');
  console.log('README updated successfully.');
} else {
  console.log('\nNo changes made to README.');
}
