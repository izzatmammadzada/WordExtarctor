# Web Word Extractor

A simple command-line tool to extract and count the most frequent words from a given webpage. The tool uses BeautifulSoup for HTML parsing and regular expressions to find words within the text.

## Features

- Fetches HTML content from a given URL.
- Extracts words and counts their frequency.
- Supports filtering words by minimum length.
- Outputs the top N words and saves them to a file if desired.

## Requirements

This project requires the following Python packages, specified in the `requirements.txt` file:

- `beautifulsoup4==4.12.3`
- `click==8.1.7`

You can install the required packages using pip:

```bash
pip install -r requirements.txt
