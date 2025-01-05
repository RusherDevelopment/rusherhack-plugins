const fs = require('fs');

const parsedBadgesPath = process.argv[2]; // Get parsed badges file path from arguments
const readmePath = 'README.md';

if (!fs.existsSync(parsedBadgesPath)) {
  console.error(`Error: Parsed badges file not found at ${parsedBadgesPath}`);
  process.exit(1);
}

// Load parsed badges and README content
const parsedBadges = JSON.parse(fs.readFileSync(parsedBadgesPath, 'utf8'));
let readmeContent = fs.readFileSync(readmePath, 'utf8');

// Generate new plugins list
const newPluginsList = parsedBadges
  .map(
    (plugin) =>
      `- [${plugin.name}](https://github.com/${plugin.repo}) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/${plugin.repo}/total)](${plugin.releaseUrl})`
  )
  .join('\n');

// Define regex to match the plugins list section
const pluginsListRegex = /<!-- START PLUGINS LIST -->([\s\S]*?)<!-- END PLUGINS LIST -->/;

// Replace the old plugins list with the new one
const updatedReadmeContent = readmeContent.replace(
  pluginsListRegex,
  `<!-- START PLUGINS LIST -->\n${newPluginsList}\n<!-- END PLUGINS LIST -->`
);

// Check if changes were made
if (updatedReadmeContent !== readmeContent) {
  fs.writeFileSync(readmePath, updatedReadmeContent);
  console.log('README updated with latest plugin list.');
  process.exit(0); // Indicate changes were made
} else {
  console.log('No changes made to README.');
  process.exit(1); // Indicate no changes were made
}
