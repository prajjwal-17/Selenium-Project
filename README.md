# Amazon Product Scraper

A comprehensive Python-based web scraper for Amazon India product pages. This project uses Selenium for automated web scraping to collect product HTML files, and BeautifulSoup for parsing and extracting product information into structured JSON format.

## Features

- 🔍 **Automated Web Scraping**: Uses Selenium to scrape Amazon India product pages
- 💾 **HTML File Storage**: Saves scraped HTML files locally for processing
- 📊 **Data Extraction**: Extracts product titles, prices, and links from HTML files
- 💼 **JSON Output**: Saves structured data to JSON format with UTF-8 encoding
- 🛡️ **Error Handling**: Robust error handling for malformed HTML files
- 📈 **Progress Tracking**: Real-time progress tracking with console output
- 🇮🇳 **Amazon India Focus**: Specifically designed for Amazon India (amazon.in)

## Project Structure

```
amazon-product-scraper/
│
├── project.py              # Main Selenium scraper (saves HTML files)
├── finalcollect.py         # HTML processor (extracts data to JSON)
├── collect.py              # Test script for development
├── locating_single.py      # Test script for single element extraction
├── locating_multiple.py    # Test script for multiple element extraction
├── data/                   # Directory containing scraped HTML files
│   ├── product1.html
│   ├── product2.html
│   └── ...
├── products.json           # Final output file with extracted data
└── README.md
```

## Requirements

- Python 3.6+
- Selenium
- BeautifulSoup4
- Chrome/Firefox WebDriver
- os (built-in)
- json (built-in)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/amazon-product-scraper.git
cd amazon-product-scraper
```

2. Install required dependencies:
```bash
pip install selenium beautifulsoup4
```

3. Install WebDriver:
   - **Chrome**: Download [ChromeDriver](https://chromedriver.chromium.org/) and add to PATH
   - **Firefox**: Download [GeckoDriver](https://github.com/mozilla/geckodriver/releases) and add to PATH

4. Create a `data` directory for storing HTML files:
```bash
mkdir data
```

## Usage

## Usage

### Step 1: Scrape Product Pages (Selenium)

First, run the main scraper to collect HTML files from Amazon:

```bash
python project.py
```

This script will:
- Launch a web browser using Selenium
- Navigate to Amazon India product pages
- Save HTML content to individual files in the `data` directory
- Handle dynamic content and page loading

### Step 2: Extract Data from HTML Files

Then, process the collected HTML files to extract structured data:

```bash
python finalcollect.py
```

This script will:
- Process all HTML files in the `data` directory
- Extract product information (title, price, link)
- Display progress in the console
- Save results to `products.json`

### Workflow

```
Amazon India → [Selenium] → HTML Files → [BeautifulSoup] → JSON Data
     ↓              ↓            ↓              ↓             ↓
  Live Pages → project.py → data/*.html → finalcollect.py → products.json
```

### Output

The script will:
1. Process all HTML files in the `data` directory
2. Extract product information (title, price, link)
3. Display progress in the console
4. Save results to `products.json`

### Sample Output

Console output:
```
Title: Apple iPhone 15 (128 GB) - Black...
Price: ₹79,900
Link: https://amazon.in/dp/B0CHX1W1XY...
--------------------------------------------------------------------------------
Title: Samsung Galaxy S24 Ultra (256 GB) - Titanium Gray...
Price: ₹1,24,999
Link: https://amazon.in/dp/B0CTWQ1H2X...
--------------------------------------------------------------------------------

Total products scraped: 25
Data saved to products.json
```

JSON output structure:
```json
[
  {
    "title": "Apple iPhone 15 (128 GB) - Black",
    "price": "₹79,900",
    "link": "https://amazon.in/dp/B0CHX1W1XY",
    "file_source": "product1.html"
  },
  {
    "title": "Samsung Galaxy S24 Ultra (256 GB) - Titanium Gray",
    "price": "₹1,24,999",
    "link": "https://amazon.in/dp/B0CTWQ1H2X",
    "file_source": "product2.html"
  }
]
```

## Test Scripts

The repository includes several test scripts for development and debugging:

- **`collect.py`** - Test script for basic data collection functionality
- **`locating_single.py`** - Test script for extracting single HTML elements
- **`locating_multiple.py`** - Test script for extracting multiple HTML elements

These scripts are used for development purposes and testing different extraction methods.

## How It Works

### Phase 1: Web Scraping (project.py)
1. **Browser Automation**: Uses Selenium to control a web browser
2. **Page Navigation**: Navigates to Amazon India product pages
3. **Dynamic Content**: Waits for pages to fully load including JavaScript content
4. **HTML Collection**: Saves complete HTML content to individual files in `data/` directory
5. **Error Handling**: Handles network issues, timeouts, and page loading errors

### Phase 2: Data Extraction (finalcollect.py)
1. **File Processing**: Iterates through all HTML files in the `data` directory
2. **HTML Parsing**: Uses BeautifulSoup to parse saved HTML content
3. **Element Extraction**:
   - Finds product title from `<h2>` tags
   - Extracts price from `<span class="a-price-whole">`
   - Constructs product link from parent anchor tag
4. **Data Cleaning**: Removes extra whitespace and formatting
5. **JSON Output**: Saves clean, structured data with proper encoding

## Data Sources

This scraper works in two phases:
1. **Live Scraping**: `project.py` uses Selenium to scrape live Amazon India product pages
2. **Local Processing**: `finalcollect.py` processes the locally saved HTML files

The scraper can handle dynamic content that loads via JavaScript, making it more robust than simple HTTP request-based scrapers.

## Error Handling

The script includes comprehensive error handling:
- Continues processing if individual files fail
- Displays error messages for debugging
- Maintains data integrity for successful extractions

## Limitations

- Requires WebDriver installation (Chrome/Firefox)
- May be affected by Amazon's anti-bot measures
- Dependent on Amazon's HTML structure (may break if Amazon changes their layout)
- Scraping speed limited by page load times and politeness delays
- Requires stable internet connection for initial scraping phase

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This tool is for educational purposes only. Please respect Amazon's robots.txt and terms of service. Be mindful of rate limiting and consider the ethical implications of web scraping.

## Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

**Note**: Make sure you have the necessary permissions to scrape the target website and comply with their terms of service.
