# Amazon Product Scraper

A Python-based web scraper for extracting product information from Amazon India product pages. This tool processes HTML files stored locally and extracts product titles, prices, and links, saving the data in JSON format.

## Features

- 🔍 Extracts product titles, prices, and links from Amazon HTML files
- 💾 Saves scraped data to JSON format with UTF-8 encoding
- 🛡️ Error handling for malformed HTML files
- 📊 Progress tracking with console output
- 🇮🇳 Specifically designed for Amazon India (amazon.in)

## Project Structure

```
amazon-product-scraper/
│
├── project.py              # Main scraper script
├── finalcollect.py         # Final collection script (duplicate of project.py)
├── collect.py              # Test script for development
├── locating_single.py      # Test script for single element extraction
├── locating_multiple.py    # Test script for multiple element extraction
├── data/                   # Directory containing HTML files to process
│   ├── product1.html
│   ├── product2.html
│   └── ...
├── products.json           # Output file with scraped data
└── README.md
```

## Requirements

- Python 3.6+
- BeautifulSoup4
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
pip install beautifulsoup4
```

3. Create a `data` directory and place your Amazon HTML files inside:
```bash
mkdir data
# Add your HTML files to the data directory
```

## Usage

### Main Script

Run the main scraper script:

```bash
python project.py
```

or

```bash
python finalcollect.py
```

Both scripts perform the same function - extracting product data from HTML files in the `data` directory.

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

1. **File Processing**: The script iterates through all files in the `data` directory
2. **HTML Parsing**: Uses BeautifulSoup to parse HTML content
3. **Element Extraction**:
   - Finds product title from `<h2>` tags
   - Extracts price from `<span class="a-price-whole">`
   - Constructs product link from parent anchor tag
4. **Data Cleaning**: Removes extra whitespace and formatting
5. **Error Handling**: Continues processing even if individual files fail
6. **Output**: Saves clean JSON data with proper encoding

## Data Sources

This scraper is designed to work with HTML files from Amazon India product pages. The HTML files should be saved locally in the `data` directory before running the script.

## Error Handling

The script includes comprehensive error handling:
- Continues processing if individual files fail
- Displays error messages for debugging
- Maintains data integrity for successful extractions

## Limitations

- Only works with Amazon India (amazon.in) product pages
- Requires pre-downloaded HTML files
- Dependent on Amazon's HTML structure (may break if Amazon changes their layout)
- Does not handle dynamic content loaded by JavaScript

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
