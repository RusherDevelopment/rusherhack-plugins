const fs = require('fs');

// Load parsed badges and README
const parsedBadges = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
let readmeContent = fs.readFileSync('README.md', 'utf8');

// Regex to match the plugins list section in the README
const sectionRegex = /## Plugins List([\s\S]*?)##/g;
const sectionMatch = sectionRegex.exec(readmeContent);

if (!sectionMatch) {
  console.error('Error: Could not find the plugins list section in the README.');
  process.exit(1);
}

let pluginsListContent = sectionMatch[1].trim();

// Regex to extract plugin names and their existing badges
const pluginRegex = /- ### \[(.+?)\]\(https:\/\/github\.com\/.+?\) <br>\s+.*?\n.*?\[!\[GitHub Downloads \(all releases\)\]\((.+?)\)\]/g;

let match;
const readmePlugins = new Map();

// Parse the plugins list to extract plugin names and badge URLs
while ((match = pluginRegex.exec(pluginsListContent)) !== null) {
  const pluginName = match[1].trim().toLowerCase(); // Normalize name for matching
  const badgeUrl = match[2].trim();
  readmePlugins.set(pluginName, badgeUrl);
}

// Log parsed plugin names from README
console.log('Parsed plugin names from README:', Array.from(readmePlugins.keys()));

// Flag to track if changes are made
let changesMade = false;

// Check and update each plugin in parsed badges
parsedBadges.forEach(({ name, repo, latestReleaseUrl }) => {
  const normalizedPluginName = name.trim().toLowerCase(); // Normalize name for matching
  if (readmePlugins.has(normalizedPluginName)) {
    console.log(`Matching plugin found in README for ${name}`);

    // Construct the expected download badge URL
    const expectedBadgeUrl = `https://img.shields.io/github/downloads/${repo}/total`;

    // Replace the existing badge URL in the README
    const currentBadgeUrl = readmePlugins.get(normalizedPluginName);
    if (currentBadgeUrl !== expectedBadgeUrl) {
      readmeContent = readmeContent.replace(currentBadgeUrl, expectedBadgeUrl);
      changesMade = true;
    }
  } else {
    console.log(`No matching plugin found in README for ${name}`);
  }
});

// Write updated plugins list back into the README if changes were made
if (changesMade) {
  console.log('Changes detected, updating README...');
  fs.writeFileSync('README.md', readmeContent, 'utf8');
  console.log('README updated successfully.');
  process.exit(0); // Indicate success
} else {
  console.log('No changes made to README.');
  process.exit(1); // Indicate no changes
}
