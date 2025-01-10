const fs = require('fs');
const path = require('path');

// Paths to badges.json and README.md
const badgesPath = path.join(__dirname, 'badges.json');
const readmePath = path.join(__dirname, 'README.md');

// Load badges.json
const badges = JSON.parse(fs.readFileSync(badgesPath, 'utf8'));

// Function to generate a plugin section
function generatePluginSection(plugin, index) {
  const screenshots = plugin.screenshots
    ? `<details>
  <summary>Show Screenshots</summary>
  <p align="center">
    ${plugin.screenshots.map(
      (url) => `<img src="${url}" alt="${plugin.name} Screenshot" border="0" width="750">`
    ).join('\n    ')}
  </p>
</details>`
    : '';

  return `
- ### [${plugin.name}](${plugin.url}) <br>

  [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[${index}].releaseDate&label=Latest%20Release&color=green)](${plugin.url}/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/${plugin.creator}/${plugin.name}/total)](${plugin.downloadsUrl})<br>

  **Creator**: <img src="${plugin.avatarUrl}" width="20" height="20"> [${plugin.creator}](${plugin.creatorUrl})

  ${plugin.description}

  ${screenshots}

---
`;
}

// Generate the Plugins List section
function generatePluginsList(badges) {
  const plugins = badges.plugins;
  let content = '<!-- START PLUGINS LIST -->\n\n';
  plugins.forEach((plugin, index) => {
    content += generatePluginSection(plugin, index);
  });
  content += '\n<!-- END PLUGINS LIST -->';
  return content;
}

// Read the existing README.md
let readmeContent = fs.readFileSync(readmePath, 'utf8');

// Replace the Plugins List section in README.md
const updatedContent = readmeContent.replace(
  /<!-- START PLUGINS LIST -->[\s\S]*<!-- END PLUGINS LIST -->/,
  generatePluginsList(badges)
);

// Write the updated content back to README.md
fs.writeFileSync(readmePath, updatedContent, 'utf8');

console.log('README.md updated successfully with the latest Plugins List!');
