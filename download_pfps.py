import os
import requests

# === CONFIG ===
# Folder to save profile pictures
PFPS_FOLDER = "pfps"

# Text file containing usernames (one per line)
USERNAMES_FILE = "usernames_only.txt"

# === SETUP ===
# Create folder if it doesn't exist
os.makedirs(PFPS_FOLDER, exist_ok=True)

# Read usernames
with open(USERNAMES_FILE, "r", encoding="utf-8") as f:
    usernames = [line.strip() for line in f if line.strip()]

print(f"Total usernames: {len(usernames)}")

# Function to get profile picture URL without login
def get_profile_pic_url(username):
    """
    Get Instagram profile picture URL in original/high quality.
    Uses public Instagram JSON endpoint (no login required).
    """
    try:
        url = f"https://www.instagram.com/{username}/?__a=1&__d=dis"
        response = requests.get(url, timeout=10)
        data = response.json()
        # Extract profile pic URL
        return data["graphql"]["user"]["profile_pic_url_hd"]
    except Exception as e:
        print(f"[❌] Skipping {username}: {e}")
        return None

# === DOWNLOAD LOOP ===
for username in usernames:
    filename = os.path.join(PFPS_FOLDER, f"{username}_profile_pic.jpg")

    # Skip if already downloaded
    if os.path.exists(filename):
        print(f"[⚠️] Already exists: {username}")
        continue

    profile_pic_url = get_profile_pic_url(username)
    if not profile_pic_url:
        continue

    try:
        response = requests.get(profile_pic_url, timeout=15)
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"[✅] Downloaded: {username}")
    except Exception as e:
        print(f"[❌] Failed {username}: {e}")
