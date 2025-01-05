const fs = require('fs');

// Read and parse badges.json
const badges = JSON.parse(fs.readFileSync('badges.json', 'utf8'));

// Extract plugin names, repo (from URL), and latest release URLs
const parsedData = badges.plugins.map(plugin => {
  const repoMatch = plugin.url.match(/github\.com\/([^/]+\/[^/]+)/);
  return {
    name: plugin.name,
    repo: repoMatch ? repoMatch[1] : null, // Extract repo as owner/repo
    latestReleaseUrl: plugin.latestReleaseUrl
  };
});

// Save parsed data to parsed-badges.json
fs.writeFileSync('parsed-badges.json', JSON.stringify(parsedData, null, 2));

console.log('Parsed badges.json and saved to parsed-badges.json');
