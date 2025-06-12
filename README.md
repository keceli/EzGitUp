# EZGitUp

A simple command-line tool to upload files to GitHub repositories.

## Installation

```bash
pip install ezgitup
```

## Usage

### Environment Variables

You can set the following environment variables:
- `GITHUB_TOKEN`: Your GitHub personal access token (required)
- `EZGITUP_DEPO`: Repository in format "owner/repo" (optional)

### Command Line Usage

Upload single or multiple files:

```bash
# Upload single file
ezgitup path/to/file.txt

# Upload multiple files
ezgitup path/to/file1.txt path/to/file2.txt
```

If no files are specified, the tool will prompt you to enter file paths interactively.

### Interactive Mode

If you don't specify any files or the `EZGITUP_DEPO` environment variable, the tool will guide you through the process:

```bash
ezgitup
```

## Features

- Upload single or multiple files to GitHub repositories
- Support for environment variables
- Interactive mode for user input
- Simple command-line interface
- Progress tracking for multiple file uploads

## Requirements

- Python 3.6 or higher
- requests library

## License

MIT License

   
