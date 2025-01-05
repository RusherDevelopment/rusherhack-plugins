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

let changesMade = false;

// Loop through each plugin and update README if necessary
parsedBadges.forEach(plugin => {
  const downloadBadgeRegex = new RegExp(
    `\\!\GitHub Downloads \all releases\\\https://img\\.shields\\.io/github/downloads/${plugin.repo}/total\.*?\`,
    'g'
  );

  const newDownloadBadge = `[![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/${plugin.repo}/total)](${plugin.releaseUrl})`;

  if (readmeContent.match(downloadBadgeRegex)) {
    readmeContent = readmeContent.replace(downloadBadgeRegex, newDownloadBadge);
    changesMade = true;
  }
});

// Save updated README if changes were made
if (changesMade) {
  fs.writeFileSync(readmePath, readmeContent);
  console.log('README updated with latest download URLs.');
  process.exit(0); // Indicate changes were made
} else {
  console.log('No changes made to README.');
  process.exit(1); // Indicate no changes were made
}
