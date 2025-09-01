import instaloader
import os

L = instaloader.Instaloader()
# L.load_session_from_file('your_instagram_username')  # optional if private profiles

os.makedirs("profile_pics", exist_ok=True)

with open("usernames_only.txt", "r", encoding="utf-8") as f:
    usernames = [line.strip() for line in f]

for username in usernames:
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        L.download_pic(f"profile_pics/{username}.jpg", profile.profile_pic_url, profile.date_joined)
    except Exception as e:
        print(f"Skipping {username}: {e}")
