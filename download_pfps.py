import os
import instaloader

# Folder to save profile pictures
SAVE_FOLDER = "pfps"
os.makedirs(SAVE_FOLDER, exist_ok=True)

# Load usernames
with open("usernames_only.txt", "r") as f:
    usernames = [line.strip() for line in f if line.strip()]

print(f"Total usernames: {len(usernames)}")

# Create Instaloader instance
L = instaloader.Instaloader(download_pictures=True, download_video_thumbnails=False,
                            download_videos=False, download_geotags=False,
                            download_comments=False, save_metadata=False,
                            post_metadata_txt_pattern="", max_connection_attempts=1)

for username in usernames:
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        filename = os.path.join(SAVE_FOLDER, f"{username}_profile_pic.jpg")
        L.download_pic(filename, profile.profile_pic_url, mtime=None)
        print(f"[✅] Downloaded: {username}")
    except Exception as e:
        print(f"[❌] Skipping {username}: {e}")
