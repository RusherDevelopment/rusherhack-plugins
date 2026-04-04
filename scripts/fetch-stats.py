import json
import os
import requests
import time

JSON_PATH = "generated/json/plugins-and-themes.json"
TOKEN = os.getenv("GITHUB_TOKEN")

def get_github_stats(repo):
    headers = {"Authorization": f"token {TOKEN}"} if TOKEN else {}
    stats = {"stars": 0, "downloads": 0}
    try:
        #Stars
        req = requests.get(f"https://api.github.com/repos/{repo}", headers=headers, timeout=10)
        if (req.status_code) == 200:#its so cool
            stats["stars"] = req.json().get("stargazers_count", 0)
        
        #Downloads
        req = requests.get(f"https://api.github.com/repos/{repo}/releases", headers=headers, timeout=10)
        if (req.status_code) == 200:
            releases = req.json()
            stats["downloads"] = sum(asset.get("download_count", 0) for release in releases for asset in release.get("assets", []))
    except Exception as e:
        print(f"Error fetching stats for {repo}: {e}")
    
    return stats

def main():
    if (not os.path.exists(JSON_PATH)):
        print(f"JSON file not found at {JSON_PATH}")
        return
    
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    print("Fetching GitHub stats...")
    for category in ["plugins", "themes"]:
        for item in data.get(category, []):
            repo = item.get("repo", "")
            if (repo and "/" in repo):
                res = get_github_stats(repo)
                item["stars"] = res["stars"]
                item["downloads"] = res["downloads"]
                time.sleep(0.05)#github delay
    
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print("Stats updated successfully.")

if __name__ == "__main__":
    main()