#I have not had the chance to test this one yet - TK 2/14/2023
usernames = {}
passwords = {}
web_portals = {}

# Read the username information from a text file
with open("usernames.txt", "r") as f:
    for line in f:
        parts = line.strip().split(",")
        username = parts[0]
        password = parts[1]
        usernames[username] = password

# Read the password information from a text file
with open("passwords.txt", "r") as f:
    for line in f:
        parts = line.strip().split(",")
        password = parts[0]
        web_portal = parts[1]
        passwords[password] = web_portal

# Read the web portal information from a text file
with open("web_portals.txt", "r") as f:
    for line in f:
        parts = line.strip().split(",")
        web_portal = parts[0]
        url = parts[1]
        web_portals[web_portal] = url

# Prompt the user for their username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

# Check if the entered username and password are valid
if username in usernames and password in passwords:
    expected_password = usernames[username]
    if expected_password != password:
        print("Incorrect password for username", username)
    else:
        web_portal = passwords[password]
        url = web_portals[web_portal]
        print("Success! Logging you into", web_portal, "at", url)
else:
    print("Invalid username or password")
