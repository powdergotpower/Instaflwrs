from instagrapi import Client

# Load session
cl = Client()
sessionid = "YOUR_SESSIONID_HERE"  # Replace with your sessionid
cl.set_settings({"sessionid": sessionid})

# Load usernames
with open("usernames_only.txt", "r", encoding="utf-8") as f:
    usernames = [line.strip() for line in f.readlines()]

profiles = []

for username in usernames:
    try:
        profile = cl.user_info_by_username(username)
        # Just get what we need: username and profile picture
        profiles.append({
            "username": username,
            "profile_pic": profile.profile_pic_url
        })
        print(f"Loaded {username}")
    except Exception as e:
        print(f"Skipping {username}: {e}")

# At this point, `profiles` contains all users with their profile pics
# You can now pass `profiles` to your battle simulation logic
print(f"\nTotal profiles loaded: {len(profiles)}")
