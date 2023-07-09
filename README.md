# Web Crawler Project

This project is a web crawler that performs various tasks, such as finding contact pages, extracting emails, and loading URLs. It provides a set of scripts that can be executed individually or combined for different use cases.

## Features

- **Find Urls**: Search for pages on google using Google Search.
- **Extract Emails**: Extract email addresses from web pages.
- **Enter data**: Enter data and submit on contact page.
- **Send emails**: Send emails to the emails on csv.

## Getting Started

### Prerequisites

- Python 3.x
- Google Chrome browser
- ChromeDriver (compatible with the installed Chrome version)

### Installation

1. Clone the repository:

```git
git clone https://github.com/Michael-Liendo/python-crawler
```

2. Navigate to the project directory:

```cd web-crawler```

3. Install the required packages

```pip install -r requirements.txt```

4. Download and install ChromeDriver from the official website: [ChromeDriver - WebDriver for Chrome](https://sites.google.com/a/chromium.org/chromedriver/)

5. Ensure that the ChromeDriver executable is in your system's PATH.

## Usage

### Find URL Pages

To find urls on google, configure `.env`, run the following command:

```bash
python3 src/main.py --load-urls
```

The script will use Google dorks to search for urls and save the results to a CSV file.

### Extract Emails

To extract email addresses from web pages, run the following command:

```bash
python3 src/main.py --extract-emails
```

The script will load URLs from a CSV file and extract email addresses from each web page.

### Enter Data

To load a list of URLs from a CSV file, run the following command:

```bash
python3 src/main.py --enter-data
```

The script will load URLs from the specified CSV file and send form contact.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
