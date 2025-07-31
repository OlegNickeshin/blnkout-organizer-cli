# 🗂️ blnkout-organizer-cli

A minimalist command-line tool to sort, inspect, and organize files in a folder. Built for clarity, speed, and control.

---

## 🚀 Features

- ✅ Organize files by **extension** into folders  
- ✅ Detect and organize only files of a **specific extension**  
- ✅ List:
  - all contents  
  - only files  
  - only folders  
- ✅ Sort files by **size**  
- ✅ Show files **larger than X MB**  
- ✅ Show files **modified in the last N days**  
- ✅ Get detailed **file info** (size, modified date, permissions, etc.)  
- ✅ 🖥️ Pretty terminal output using `rich`

---

## 📦 Installation

```bash
git clone https://github.com/olegnickeshin/blnkout-organizer-cli.git
cd blnkout-organizer-cli
pip install .
```

You will get a command-line tool named `blnk-org`.

---

## 🛠️ Usage

```bash
blnk-org <folder_path> [options]
```

### 🔹 Examples:

```bash
blnk-org ~/Downloads --ext-all                     # Organize all files by extension
blnk-org ~/Documents --ext pdf                     # Move all .pdf files into ./pdf/
blnk-org ~/Desktop --file-size 5                   # List files > 5MB
blnk-org ~/Projects --sort-size                    # Sort files by size
blnk-org ~/Notes --modified-after 3                # Files modified in the last 3 days
blnk-org ~/Files --file-info "report.pdf"          # Show detailed info for report.pdf
blnk-org ~/Stuff --list                            # List all files and folders
blnk-org ~/Stuff --list-files                      # List only files
blnk-org ~/Stuff --list-dirs                       # List only folders
```

---

## 💡 Command Reference

| Flag                | Description                                 |
|---------------------|---------------------------------------------|
| `--ext`             | Organize files with a specific extension    |
| `--ext-all`         | Organize all files by extension             |
| `--file-size`       | Show files larger than X MB                 |
| `--sort-size`       | Sort files by size (largest first)          |
| `--modified-after`  | Show files modified in last N days          |
| `--file-info`       | Show details for a specific file            |
| `--list`            | List all contents                           |
| `--list-files`      | List only files                             |
| `--list-dirs`       | List only folders                           |

---

## 🧪 Requirements

- Python 3.7+
- [`rich`](https://github.com/Textualize/rich)

---

## 📝 License

MIT
