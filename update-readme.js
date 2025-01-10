const fs = require('fs');
const path = require('path');

const badgesPath = './badges.json';
const readmePath = './README.md';

function generatePluginSection(badges) {
  let section = `## Plugins List\n\nTotal Plugins: ${badges.totalPlugins.message}\n\n`;
  
  section += `| Name | Description | Latest Release |\n`;
  section += `|------|-------------|----------------|\n`;
  
  badges.plugins.forEach(plugin => {
    section += `| [${plugin.name}](${plugin.url}) | ${plugin.description} | [Download](${plugin.latestReleaseUrl}) |\n`;
  });

  return section;
}

function updateReadme() {
  if (!fs.existsSync(badgesPath)) {
    console.error('Error: badges.json not found.');
    process.exit(1);
  }

  const badges = JSON.parse(fs.readFileSync(badgesPath, 'utf8'));
  const newSection = generatePluginSection(badges);

  let readmeContent = fs.readFileSync(readmePath, 'utf8');
  const startMarker = '<!-- START PLUGINS LIST -->';
  const endMarker = '<!-- END PLUGINS LIST -->';

  const newContent = `${startMarker}\n${newSection}\n${endMarker}`;
  readmeContent = readmeContent.replace(new RegExp(`${startMarker}[\\s\\S]*${endMarker}`), newContent);

  fs.writeFileSync(readmePath, readmeContent, 'utf8');
  console.log('README.md updated successfully.');
}

updateReadme();
