import os
import requests

# Folder to save profile pictures
os.makedirs("pfps", exist_ok=True)

for username in usernames:
    # Get profile picture URL for this username (from your API or method)
    profile_pic_url = get_profile_pic_url(username)  # replace with your method
    
    # Define file name with username
    filename = f"pfps/{username}_profile_pic.jpg"
    
    # Download and save
    response = requests.get(profile_pic_url)
    with open(filename, "wb") as f:
        f.write(response.content)
    
    print(f"[✅] Downloaded: {username}")
