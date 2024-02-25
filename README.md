# Crypto Wallet Balance Scraper

Simple project based on Python that allows you to scrape and analyze the balances of cryptocurrency wallets from a specified blockchain explorer.


## Usage

1. **Prepare the Input File**: Create a text file (e.g., `wallets.txt`) and add the cryptocurrency wallet addresses you want to analyze. Each address should be on a separate line.

2. **Run the Scraper**:
   - Execute the `main.py` script to start the scraping process.

3. **Review the Results**:
   - Check the `output` folder for the results, including the log file and the file containing wallet addresses with balances.

## Extending for Other Cryptocurrencies or Blockchains

You can easily extend this project to support other cryptocurrencies or blockchains by following these steps:

1. Create a new module in the `modules` directory for the specific cryptocurrency.
2. Define scraping functions tailored to that cryptocurrency.
3. Add a configuration section in `config.json`
