const fs = require('fs');

// Read and parse badges.json
const badges = JSON.parse(fs.readFileSync('badges.json', 'utf8'));

// Extract plugin names, derived repo, and latest release URLs
const parsedData = badges.plugins.map((plugin) => {
  const repoMatch = plugin.url.match(/github\.com\/([^/]+\/[^/]+)/);
  const repo = repoMatch ? repoMatch[1] : null;
  return {
    name: plugin.name,
    repo: repo,
    latestReleaseUrl: plugin.latestReleaseUrl,
  };
});

fs.writeFileSync('parsed-badges.json', JSON.stringify(parsedData, null, 2));
console.log('Parsed badges.json and saved to parsed-badges.json');
