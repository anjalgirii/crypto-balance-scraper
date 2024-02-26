# Crypto Wallet Balance Scraper

Simple project based on Python that allows you to scrape and analyze the balances of cryptocurrency wallets from a specified blockchain explorer.

## Usage

1. **Run the Scraper**:
   - Execute the `main.py` script to start the scraping process.

2. **Prepare the Input File**: Drag n drop files or folders on the terminal.

3. **Review the Results**:
   - Check the `output` folder for the results.
---

## Changelog

### Version 1.1.0 (February 25, 2024)

#### Added
- Ability to extract cryptocurrency addresses from any directory.
- Balance check functionality for Bitcoin (BTC).
- Output folder to store results.

#### Changed
- Updated address identifier.

#### Fixed
- Some minor bugs.

---

## Extending for Other Cryptocurrencies or Blockchains

You can easily extend this project to support other cryptocurrencies or blockchains by following these steps:

1. Create a new module in the `modules` directory for the specific cryptocurrency.
2. Define scraping functions tailored to that cryptocurrency.
3. Add a configuration section in `config.json`.
