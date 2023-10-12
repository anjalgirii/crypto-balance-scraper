# Crypto Wallet Balance Scraper

The Crypto Wallet Balance Scraper is a Python project that allows you to scrape and analyze the balances of cryptocurrency wallets from a specified blockchain explorer. The project is organized into separate modules for flexibility and extensibility.

## Project Structure

The project is structured as follows:

- `main.py`: The main script that reads wallet addresses from an input file, scrapes wallet balances, and saves the results.

- `modules` directory:
    - `eth.py`: A module containing Ethereum-specific scraping functions.
    - `file_handler.py`: A module to handle file input and output operations.
    - `web_scraper.py`: A generic module for web scraping functions that can be used for multiple cryptocurrencies.

- `config` directory:
    - `config.json`: A configuration file that stores the URLs and other parameters specific to each supported cryptocurrency or blockchain.

- `input.txt`: An input file containing a list of cryptocurrency wallet addresses to be analyzed.

- `output` directory: The results of the scraping process are saved in this directory.

## Usage

1. **Prepare the Input File**: Create a text file (e.g., `wallets.txt`) and add the cryptocurrency wallet addresses you want to analyze. Each address should be on a separate line.

2. **Run the Scraper**:
   - Execute the `main.py` script to start the scraping process.

3. **Review the Results**:
   - Check the `output` folder for the results, including the log file and the file containing wallet addresses with non-zero balances.

## Extending for Other Cryptocurrencies or Blockchains

You can easily extend this project to support other cryptocurrencies or blockchains by following these steps:

1. Create a new module in the `modules` directory for the specific cryptocurrency.
2. Define scraping functions tailored to that cryptocurrency.
3. Add a configuration section in `config.json`
