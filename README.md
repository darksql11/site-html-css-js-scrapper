# Proxy Scraper README

## Introduction

This Python script is a **Proxy Scraper** designed to download and parse web pages recursively from a given **start URL**. It extracts and saves **HTML, JavaScript (JS), and CSS files** into designated folders.

## Features

- **Multi-threaded Execution:** Uses `ThreadPoolExecutor` for faster performance.
- **Recursive Crawling:** Extracts links from visited pages and continues crawling.
- **File Categorization:** Saves **HTML, JS, and CSS** files into separate directories.
- **User-Agent Spoofing:** Uses a **Mozilla User-Agent** to mimic a real browser.
- **Timeout Handling:** Prevents hanging on slow or unresponsive requests.

## Prerequisites

Ensure you have **Python 3.x** installed and install the required dependencies:

```bash
pip install requests beautifulsoup4
```

## Installation & Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-repo/proxy-scraper.git
   cd proxy-scraper
   ```
2. **Modify ****`start_url`** in the script:
   ```python
   start_url = "https://example.com"  # Replace with your target site
   ```
3. **Run the script:**
   ```bash
   python scraper.py
   ```

## Configuration

You can change the following parameters in the script:

- **Folders for storing files:**
  ```python
  html_folder = "html_files"  # Folder for HTML files
  js_folder = "js_files"      # Folder for JS files
  css_folder = "css_files"    # Folder for CSS files
  ```
- **Thread count (parallel execution):**
  ```python
  ThreadPoolExecutor(max_workers=10)
  ```
  Increase or decrease the number depending on system performance.

## Output

- Downloaded **HTML, JS, and CSS** files are stored in their respective folders.
- A **summary report** is displayed at the end, showing the total number of files downloaded.

## Error Handling

- If a page fails to load, it logs an error message.
- If a JS or CSS file cannot be downloaded, it logs an error and continues.

## Example Output

```
HTML: index.html downloaded!
JS: script.js downloaded!
CSS: style.css downloaded!
Total 10 HTML, 15 JS, 8 CSS files downloaded!
Files are in: html_files, js_files, css_files
```

## License

This project is **MIT Licensed**. You are free to use and modify it.

## Contributing

Feel free to open **pull requests** or report issues on GitHub!

---

*Maked by darksql11*

