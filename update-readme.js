const fs = require('fs');

const parsedBadgesPath = process.argv[2];
const readmePath = 'README.md';

if (!fs.existsSync(parsedBadgesPath)) {
  console.error(`Error: Parsed badges file not found at ${parsedBadgesPath}`);
  process.exit(1);
}

// Load parsed badges and README content
const parsedBadges = JSON.parse(fs.readFileSync(parsedBadgesPath, 'utf8'));
let readmeContent = fs.readFileSync(readmePath, 'utf8');

let changesMade = false;

parsedBadges.forEach((plugin) => {
  const badgeRegex = new RegExp(
    `\\\!\GitHub Downloads \all releases\\\https:\\/\\/img\\.shields\\.io\\/github\\/downloads\\/${plugin.repo}\\/total\\\https:\\/\\/github\\.com\\/${plugin.repo}\\/releases\\/download\\/.*\`,
    'g'
  );

  const newBadgeLine = `[![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/${plugin.repo}/total)](${plugin.latestReleaseUrl})`;

  console.log(`Checking plugin: ${plugin.name}`);
  console.log(`Expected badge line: ${newBadgeLine}`);

  if (badgeRegex.test(readmeContent)) {
    console.log(`Badge found for ${plugin.name}. Updating...`);
    readmeContent = readmeContent.replace(badgeRegex, newBadgeLine);
    changesMade = true;
  } else {
    console.log(`No matching badge found for ${plugin.name}.`);
  }
});

if (changesMade) {
  fs.writeFileSync(readmePath, readmeContent);
  console.log('README updated with latest download URLs.');
  process.exit(0); // Indicate changes were made
} else {
  console.log('No changes made to README.');
  process.exit(1); // Indicate no changes were made
}
