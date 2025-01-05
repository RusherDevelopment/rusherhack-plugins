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

// Define regex to match the plugins list section
const pluginsListRegex = /<!-- START PLUGINS LIST -->([\s\S]*?)<!-- END PLUGINS LIST -->/;
const existingPluginsMatch = readmeContent.match(pluginsListRegex);

if (!existingPluginsMatch) {
  console.error('Error: Could not find plugins list section in README.');
  process.exit(1);
}

let existingPluginsList = existingPluginsMatch[1];
let changesMade = false;

// Update download URLs if they differ
parsedBadges.forEach((plugin) => {
  const pluginRegex = new RegExp(
    `- \${plugin.name}\\https://github\\.com/${plugin.repo}\ \!\GitHub Downloads \all releases\\\https://img\\.shields\\.io/github/downloads/${plugin.repo}/total\\\.*?\`,
    'g'
  );

  const newPluginEntry = `- [${plugin.name}](https://github.com/${plugin.repo}) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/${plugin.repo}/total)](${plugin.releaseUrl})`;

  if (existingPluginsList.match(pluginRegex)) {
    existingPluginsList = existingPluginsList.replace(pluginRegex, newPluginEntry);
    changesMade = true;
  }
});

// Replace the plugins list in the README
const updatedReadmeContent = readmeContent.replace(
  pluginsListRegex,
  `<!-- START PLUGINS LIST -->\n${existingPluginsList}\n<!-- END PLUGINS LIST -->`
);

// Check if changes were made
if (changesMade) {
  fs.writeFileSync(readmePath, updatedReadmeContent);
  console.log('README updated with latest download URLs.');
  process.exit(0); // Indicate changes were made
} else {
  console.log('No changes made to README.');
  process.exit(1); // Indicate no changes were made
}
