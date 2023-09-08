# GitUp ⬆️
A mostly *unnecessary* tool that utilizes the GitHub API to upload files to a repository directly without the need for local git commands.

## Features

- Upload files directly to your GitHub repository.
- Uses GitHub API for secure and efficient file uploads.
- No need to clone the repo or use git commands locally.

## Usage

1. Set your GitHub token as an environment variable for security:
   ```bash
   export GITHUB_TOKEN=your_github_token_here
   ```
2. Download the python script
   ```bash
   wget https://raw.githubusercontent.com/keceli/gitup/main/gitup.py
   ```
3. Run the script and follow the prompts to fill in your username or organization name, repo name, and file path.
   ```bash
   python github_uploader
   ```

## Why this is unneccessary?
Well, you should better use `git`. If for some reason you don't want to use git, you could do also do this with `curl`:
```bash
curl -X PUT -H "Authorization: token YOUR_GITHUB_TOKEN" \
-d '{"message": "YOUR_COMMIT_MESSAGE", "content": "BASE64_ENCODED_CONTENT"}' \
https://api.github.com/repos/OWNER/REPO_NAME/contents/PATH_TO_FILE
```
But, note that the file needs to be encoded with Base64, which can be done with `base64` on linux.

## Why this might be useful
The conversion can be tricky sometimes and you may get invalid encoding error. Python `base64` module handles the conversion.

   
