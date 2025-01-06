const fs = require('fs');

// Load README
const readmeContent = fs.readFileSync('README.md', 'utf8');

// Regex to match the plugins list section in the README
const sectionRegex = /<!-- START PLUGINS LIST -->([\s\S]*?)<!-- END PLUGINS LIST -->/;
const sectionMatch = sectionRegex.exec(readmeContent);

if (!sectionMatch) {
  console.error('Error: Could not find the plugins list section in the README.');
  process.exit(1);
}

const pluginsListContent = sectionMatch[1].trim();

// Regex to match individual plugin entries
const pluginRegex = /- ### \[(.+?)\]/g;
const pluginNames = [];

let match;
while ((match = pluginRegex.exec(pluginsListContent)) !== null) {
  pluginNames.push(match[1].trim());
}

// Log parsed plugin names
console.log('Parsed plugin names from README:', pluginNames);

if (pluginNames.length === 0) {
  console.error('No plugins were found. Please check the README format.');
  process.exit(1);
}
