const fs = require('fs');

// Load parsed badges and README content
const parsedBadges = JSON.parse(fs.readFileSync('parsed-badges.json', 'utf8'));
let readmeContent = fs.readFileSync('README.md', 'utf8');

// Define regex to match each plugin's download badge in README
parsedBadges.forEach(plugin => {
  const downloadBadgeRegex = new RegExp(
    `\\\!\GitHub Downloads \all releases\\\https:\\/\\/img\\.shields\\.io\\/github\\/downloads\\/${plugin.repo}\\/total\\\https:\\/\\/github\\.com\\/${plugin.repo}\\/releases\\/download.*?\`,
    'g'
  );

  const newDownloadBadge = `[![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/${plugin.repo}/total)](${plugin.latestReleaseUrl})`;

  // Replace the old badge with the new one if it differs
  readmeContent = readmeContent.replace(downloadBadgeRegex, newDownloadBadge);
});

// Check if changes were made
if (readmeContent !== fs.readFileSync('README.md', 'utf8')) {
  fs.writeFileSync('README.md', readmeContent);
  console.log('README updated with the latest download URLs.');
  process.exit(0); // Indicate changes were made
} else {
  console.log('No changes made to README.');
  process.exit(1); // Indicate no changes were made
}
