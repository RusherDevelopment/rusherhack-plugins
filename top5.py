import json
import requests
import re

# Load the badges.json file
with open("badges.json", "r") as file:
    data = json.load(file)

# Extract plugin entries
plugins = data["plugins"]

# Dictionary to store plugin download counts
plugin_downloads = []

# Iterate through each plugin to fetch download count
for plugin in plugins:
    name = plugin["name"]
    creator = plugin["creator"]["name"]
    description = plugin["description"]
    url = plugin["url"]

    # Extract username and repo from the GitHub URL (e.g., https://github.com/username/repo)
    repo_match = re.search(r"https://github.com/([^/]+)/([^/]+)", url)
    if repo_match:
        username, repo = repo_match.groups()
        # Construct the shields.io badge URL used in plugins.md
        badge_url = f"https://img.shields.io/github/downloads/{username}/{repo}/total.json"
        try:
            response = requests.get(badge_url)
            if response.status_code == 200:
                badge_data = response.json()
                # The download count is in the "value" field of the badge response
                download_count = int(badge_data.get("value", 0))
            else:
                print(f"Failed to fetch badge for {username}/{repo}: {response.status_code}")
                download_count = 0
        except Exception as e:
            print(f"Error fetching badge for {username}/{repo}: {e}")
            download_count = 0
    else:
        print(f"Invalid GitHub URL for {name}: {url}")
        download_count = 0

    plugin_downloads.append({
        "name": name,
        "creator": creator,
        "description": description,
        "downloads": download_count,
        "badge": f"![GitHub Downloads](https://img.shields.io/github/downloads/{username}/{repo}/total)"
    })

# Sort plugins by download count (descending) and get top 5
top_5_plugins = sorted(plugin_downloads, key=lambda x: x["downloads"], reverse=True)[:5]

# Print the top 5 plugins for manual addition to plugins.md
print("Top 5 Downloaded Plugins:")
print("| Name | Creator | Description | Downloads |")
print("|------|---------|-------------|-----------|")
for plugin in top_5_plugins:
    print(f"| {plugin['name']} | {plugin['creator']} | {plugin['description']} | {plugin['badge']} |")
