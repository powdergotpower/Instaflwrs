# download_pfps.py
import instaloader
import os

# Folder to save profile pictures
SAVE_FOLDER = "pfps"
os.makedirs(SAVE_FOLDER, exist_ok=True)

# Initialize Instaloader
L = instaloader.Instaloader(
    dirname_pattern=SAVE_FOLDER,  # save in SAVE_FOLDER
    download_videos=False,
    download_video_thumbnails=False,
    download_comments=False,
    save_metadata=False,
    post_metadata_txt_pattern="",  # no extra metadata files
)

# Read usernames
with open("usernames_only.txt", "r") as f:
    usernames = [line.strip() for line in f if line.strip()]

for username in usernames:
    try:
        # Download profile picture only
        L.download_profile(username, profile_pic_only=True)
        print(f"[✅] Downloaded: {username}")
        
        # Move the profile pic to SAVE_FOLDER root
        folder_path = os.path.join(SAVE_FOLDER, username)
        for file in os.listdir(folder_path):
            src = os.path.join(folder_path, file)
            dst = os.path.join(SAVE_FOLDER, f"{username}.jpg")
            os.rename(src, dst)
        os.rmdir(folder_path)  # remove empty folder

    except Exception as e:
        print(f"[❌] Skipping {username}: {e}")

print(f"\nDone! All profile pictures are in the '{SAVE_FOLDER}' folder.")
