import os
import requests

# Folder to save profile pictures
SAVE_FOLDER = "profile_pics"
os.makedirs(SAVE_FOLDER, exist_ok=True)

# Read usernames
with open("usernames_only.txt", "r", encoding="utf-8") as f:
    usernames = [line.strip() for line in f if line.strip()]

print(f"Total usernames: {len(usernames)}")

for username in usernames:
    try:
        # Instagram public profile URL for JSON
        url = f"https://www.instagram.com/{username}/?__a=1&__d=dis"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        response = requests.get(url, headers=headers)
        data = response.json()

        # Extract profile picture URL
        pic_url = data['graphql']['user']['profile_pic_url_hd']

        # Download the image
        img_data = requests.get(pic_url).content
        filename = os.path.join(SAVE_FOLDER, f"{username}.jpg")
        with open(filename, "wb") as img_file:
            img_file.write(img_data)
        
        print(f"Downloaded: {username}")
    
    except Exception as e:
        print(f"Skipping {username}: {e}")
