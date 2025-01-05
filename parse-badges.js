const fs = require('fs');

// Read and parse badges.json
const badges = JSON.parse(fs.readFileSync('badges.json', 'utf8'));

// Extract plugin names and latest release URLs
const parsedData = badges.plugins.map(plugin => ({
  name: plugin.name,
  repo: plugin.repo,
  latestReleaseUrl: plugin.latestReleaseUrl // Correct key for latest release URL
}));

// Save parsed data to parsed-badges.json
fs.writeFileSync('parsed-badges.json', JSON.stringify(parsedData, null, 2));

console.log('Parsed badges.json and saved to parsed-badges.json');
