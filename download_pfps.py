import os
import shutil
import instaloader

# --- Step 1: Clean old folder ---
PFPS_DIR = "pfps"
if os.path.exists(PFPS_DIR):
    shutil.rmtree(PFPS_DIR)
os.makedirs(PFPS_DIR, exist_ok=True)

# --- Step 2: Initialize Instaloader ---
L = instaloader.Instaloader(
    dirname_pattern=PFPS_DIR,
    download_videos=False,
    download_video_thumbnails=False,
    download_comments=False,
    save_metadata=False,
    post_metadata_txt_pattern="",
    quiet=True,
)

# --- Step 3: Read usernames ---
with open("usernames_only.txt", "r") as f:
    usernames = [line.strip() for line in f if line.strip()]

print(f"Total usernames: {len(usernames)}")

# --- Step 4: Download profile pics ---
for username in usernames:
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        # Save profile pic with username in filename
        filename = os.path.join(PFPS_DIR, f"{username}_profile_pic.jpg")
        L.download_pic(filename, profile.profile_pic_url, mtime=None)
        print(f"[✅] Downloaded: {username}")
    except Exception as e:
        print(f"[❌] Skipping {username}: {e}")
