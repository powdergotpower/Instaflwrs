import re

# Function to check if a line is a valid username
def is_valid_username(line):
    # Instagram usernames: letters, numbers, underscores, dots, 1-30 chars
    # Ignore lines with emojis or mostly symbols
    pattern = r'^[a-zA-Z0-9._]{1,30}$'
    return re.match(pattern, line) is not None

# Read all lines from the file
with open("all_users.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

# Remove unwanted headers
lines = [line for line in lines if line.lower() not in ("followers", "search")]

# Take every other line starting from the first one (usernames)
raw_usernames = lines[::2]

# Filter out invalid usernames
usernames = [u for u in raw_usernames if is_valid_username(u)]

# Save usernames to a new file
with open("usernames_only.txt", "w", encoding="utf-8") as f:
    for u in usernames:
        f.write(u + "\n")

print(f"Total usernames extracted: {len(usernames)}")
print("Usernames saved to 'usernames_only.txt'")
