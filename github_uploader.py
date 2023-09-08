import os
import base64
import requests

# Get the GitHub token from environment variable
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
if not GITHUB_TOKEN:
    raise ValueError("Please set your GITHUB_TOKEN as an environment variable, i.e. export GITHUB_TOKEN=xxx")

# Ask the user for the repository details and file path
owner = input("Enter the GitHub repository owner (username or organization name): ")
repo = input("Enter the repository name: ")
file_path = input("Enter the path to the file you want to upload: ")

# Read file contents and encode in base64
with open(file_path, 'rb') as file:
    content = base64.b64encode(file.read()).decode('utf-8')

# Prepare the API request
url = f"https://api.github.com/repos/{owner}/{repo}/contents/{os.path.basename(file_path)}"
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}
data = {
    "message": f"Adding file: {os.path.basename(file_path)}",
    "content": content
}

response = requests.put(url, headers=headers, json=data)

if response.status_code == 201:
    print(f"Successfully added {os.path.basename(file_path)} to the repository!")
else:
    print(f"Error: {response.json().get('message')}")
