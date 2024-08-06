import requests
import json
from github import Github
import os

# Get the GitHub token from the environment variable
ACCESS_TOKEN = os.getenv('GH_TOKEN')

# Load the existing badges.json file from the gh-pages branch
response = requests.get('https://garlicrot.github.io/RusherHacks-Plugin-Collection/badges.json')
data = response.json()

# List of plugin repositories to update
repos = [
    ("2b2t.vc-rusherhack", "rfresh2"),
    ("RusherHack-CustomHUDElement", "Aspect-404"),
    ("AutoAnvilRename", "IceTank"),
    ("QueueManager", "GabiRP"),
    ("rusherhack-instance-info", "John200410"),
    ("op-plugin", "theoplegends"),
    ("StashMoverPlugin", "xyzbtw"),
    ("unified-modulelist", "czho"),
    ("ContainerTweaks-rusherhack", "rfresh2"),
    ("rusherhack-spotify", "John200410"),
    ("Rusherhack-Vanilla-Efly", "FBanna"),
    ("rusherGUI", "xyzbtw"),
    ("Rusherhack-BookBot", "Aspect-404"),
    ("ShaysRusherTweaks", "ShayBox"),
    ("Nuker", "beanbag44"),
    ("hold-rusher", "cherosin"),
    ("NoWalkAnimation", "Eonexe"),
    ("rusherhack-nbt-utils", "kybe236"),
    ("rusherhack-executer", "kybe236"),
    ("f3-spoof", "Doogie13"),
    ("rusherhack-open-folder", "kybe236"),
    ("rusherhack-mace-kill", "kybe236"),
    ("WeatherChangingPlugin", "Lokfid"),
    ("rusherhack-middleclick-wind-charge", "kybe236"),
    ("GarlicSight", "GarlicRot"),
    ("LightningPop", "GarlicRot"),
    ("AutoBucket", "GarlicRot"),
    ("NBT-viewer", "Gentleman2292"),
    ("rusherhack-remote-controle", "kybe236"),
    ("RusherHackSpeedMeasure", "Lokfid"),
    ("rusher-tnt-bomber", "kybe236"),
    ("norender-entities", "John200410"),
    ("rusherhack-messenger", "Gentleman2292"),
]

# Authenticate to GitHub
g = Github(ACCESS_TOKEN)

# Update the release dates for each repository
for i, (repo_name, user) in enumerate(repos):
    try:
        repo = g.get_repo(f"{user}/{repo_name}")
        releases = repo.get_releases()
        latest_release = releases[0] if releases.totalCount > 0 else None

        if latest_release:
            release_date = latest_release.published_at.strftime('%Y-%m-%d')
        else:
            release_date = "No releases"

        # Update the JSON data
        data['plugins'][i]['releaseDate'] = release_date

    except Exception as e:
        print(f"Failed to update {user}/{repo_name}: {e}")

# Save the updated badges.json file
with open('badges.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Badges updated successfully.")
