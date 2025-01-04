const fs = require('fs');
const badges = JSON.parse(fs.readFileSync('badges.json', 'utf8'));
const readmePath = 'README.md';
let readmeContent = fs.readFileSync(readmePath, 'utf8');

badges.plugins.forEach(plugin => {
  const downloadBadgeRegex = new RegExp(
    `\!\GitHub Downloads \all releases\\\https://img\\.shields\\.io/github/downloads/${plugin.repo}/total\.*?\`,
    'g'
  );

  const newDownloadBadge = `[![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/${plugin.repo}/total)](${plugin.releaseUrl})`;

  readmeContent = readmeContent.replace(downloadBadgeRegex, newDownloadBadge);
});

fs.writeFileSync(readmePath, readmeContent);
console.log('README updated with latest download URLs.');
