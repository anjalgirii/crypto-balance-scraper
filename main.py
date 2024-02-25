import os
import datetime
from configparser import ConfigParser
from modules import eth, btc, address_extractor, file_handler, address_identifier

def main():
    folder_path = input("Enter the directory path for address extraction: ")

    if not os.path.isdir(folder_path):
        print(f"Error: The specified directory '{folder_path}' does not exist.")
        return

    # Load settings from settings.ini
    config = ConfigParser()
    config.read('config/settings.ini')
    check_eth = config.getboolean('Settings', 'check_eth', fallback=True)
    check_btc = config.getboolean('Settings', 'check_btc', fallback=True)

    current_date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    output_folder = os.path.join('output', current_date)
    os.makedirs(output_folder, exist_ok=True)

    extracted_addresses_filename = os.path.join(output_folder, 'extracted_addresses.txt')
    final_output_filename = os.path.join(output_folder, 'final_output_with_balances.txt')

    address_results = address_extractor.walk_and_extract_addresses(folder_path)
    for file_path, wallet, address_type in address_results:
        file_handler.write_output_to_file(extracted_addresses_filename, wallet)

    wallet_addresses = file_handler.read_wallet_addresses(extracted_addresses_filename)

    for wallet in wallet_addresses:
        address_type = address_identifier.identify_address_type(wallet)
        if address_type == "ETH" and check_eth:
            balance = eth.get_balance(wallet, "eth")
            process_balance(wallet, balance, final_output_filename)
        elif address_type == "BTC" and check_btc:
            balance = btc.get_balance(wallet)
            process_balance(wallet, balance, final_output_filename)

    print(f"Processing completed. Results are saved in the '{output_folder}' folder.")

def process_balance(wallet, balance, final_output_filename):
    if balance and not balance.startswith("Error"):
        output_message = f"Wallet: {wallet}, Balance: {balance}"
        print(output_message)
        file_handler.write_output_to_file(final_output_filename, output_message)
    else:
        print(f"Error retrieving balance for wallet: {wallet}")

if __name__ == "__main__":
    main()