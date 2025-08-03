# IKEA Product Scraper

A simple Python scraper that collects product data from the IKEA Germany website based on a search query and saves the results to a CSV file.

## Features

- Search IKEA products by keyword.
- Parse multiple pages of results.
- Extract product title, description, price, and link.
- Save results to a CSV file with a timestamped filename.
- Runs headlessly with Selenium and ChromeDriver.

## Requirements

- Python 3.8+
- Google Chrome installed
- `pip install -r requirements.txt` (requirements below)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ikea-scraper.git
   cd ikea-scraper
   ```

2. Install dependencies:
   ```bash
   pip install selenium pandas webdriver-manager
   ```

## Usage

Run the script:
```bash
python main.py
```

You will be prompted to enter:
- A search query (e.g., `stuhl`)
- Number of pages to scrape

The results will be saved to a CSV file in the `data/` folder with a name like `stuhl_ikea_2025-08-03.csv`.

## Notes

- The scraper uses a headless Chrome browser via Selenium.
- A delay (`sleep(6)`) is added after loading each page to allow content to fully load.
- Logging messages will inform about the progress and any issues.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
