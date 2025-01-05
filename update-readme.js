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

// Extract the plugins list section
const pluginsListRegex = /<!-- START PLUGINS LIST -->([\s\S]*?)<!-- END PLUGINS LIST -->/;
const match = readmeContent.match(pluginsListRegex);

if (!match) {
  console.error('Error: Plugins list section not found in README.');
  process.exit(1);
}

let pluginsSection = match[1];
let changesMade = false;

// Process each plugin from parsed badges
parsedBadges.forEach((plugin) => {
  if (!plugin.repo || !plugin.latestReleaseUrl) {
    console.log(`Skipping plugin: ${plugin.name} due to missing repo or URL.`);
    return;
  }

  const badgeRegex = new RegExp(
    `\\\!\GitHub Downloads \all releases\\\https:\\/\\/img\\.shields\\.io\\/github\\/downloads\\/${plugin.repo}\\/total\\\https:\\/\\/github\\.com\\/${plugin.repo}\\/releases\\/download\\/[^)]+\`,
    'g'
  );

  const newBadgeLine = `[![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/${plugin.repo}/total)](${plugin.latestReleaseUrl})`;

  console.log(`Checking plugin: ${plugin.name}`);
  console.log(`Expected badge line: ${newBadgeLine}`);

  if (badgeRegex.test(pluginsSection)) {
    console.log(`Badge found for ${plugin.name}. Updating...`);
    pluginsSection = pluginsSection.replace(badgeRegex, newBadgeLine);
    changesMade = true;
  } else {
    console.log(`No matching badge found for ${plugin.name}.`);
  }
});

if (changesMade) {
  // Replace the old plugins list section with the updated one
  readmeContent = readmeContent.replace(
    pluginsListRegex,
    `<!-- START PLUGINS LIST -->\n${pluginsSection}\n<!-- END PLUGINS LIST -->`
  );
  fs.writeFileSync(readmePath, readmeContent);
  console.log('README updated with latest download URLs.');
  process.exit(0);
} else {
  console.log('No changes made to README.');
  process.exit(1);
}
