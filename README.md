# blnkout-organizer-cli

A command-line tool to sort, view, and manage files in a folder.

## Features

- Organize files by extension
- Sort files by size
- List all files or only folders
- Filter by modification date
- Pretty terminal output (via `rich`)

## Install

```bash
git clone https://github.com/olegnickeshin/blnkout-organizer-cli.git
cd blnkout-organizer-cli
pip install .
```

## Usage

```bash
blnk-org ~/Downloads --sort-size
blnk-org ~/Documents --file-info "report.pdf"
```

## License

MIT
