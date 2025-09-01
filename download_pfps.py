import os
import shutil
import instaloader

PFPS_DIR = "pfps"

# Remove old folder
if os.path.exists(PFPS_DIR):
    shutil.rmtree(PFPS_DIR)
os.makedirs(PFPS_DIR, exist_ok=True)

# Initialize Instaloader
L = instaloader.Instaloader(
    download_videos=False,
    download_video_thumbnails=False,
    download_comments=False,
    save_metadata=False,
    post_metadata_txt_pattern="",
    quiet=True,
)

# Read usernames
with open("usernames_only.txt", "r") as f:
    usernames = [line.strip() for line in f if line.strip()]

print(f"Total usernames: {len(usernames)}")

# Download profile pics
for username in usernames:
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        filename = os.path.join(PFPS_DIR, f"{username}_profile_pic.jpg")
        # Directly download profile pic without using timestamp
        L.download_pic(filename, profile.profile_pic_url, mtime=None)
        print(f"[✅] Downloaded: {username}")
    except Exception as e:
        print(f"[❌] Skipping {username}: {e}")
