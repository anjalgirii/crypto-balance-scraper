import os
import datetime
from configparser import ConfigParser
from modules import eth, btc, ltc, address_extractor, file_handler

def main():
    input_path = input("Enter the directory or file path for address extraction: ")

    if not os.path.exists(input_path):
        print(f"Error: The specified path '{input_path}' does not exist.")
        return

    config = ConfigParser()
    config.read('config/settings.ini')
    check_eth = config.getboolean('Settings', 'check_eth', fallback=True)
    check_btc = config.getboolean('Settings', 'check_btc', fallback=True)
    check_ltc = config.getboolean('Settings', 'check_ltc', fallback=True)

    current_date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    output_folder = os.path.join('output', current_date)
    os.makedirs(output_folder, exist_ok=True)

    extracted_addresses_filename = os.path.join(output_folder, 'extracted_addresses.txt')
    final_output_filename = os.path.join(output_folder, 'final_output_with_balances.txt')

    if os.path.isdir(input_path):
        address_results = address_extractor.walk_and_extract_addresses(input_path)
    elif os.path.isfile(input_path):
        address_results = address_extractor.extract_addresses_from_file(input_path)
    else:
        print("Unsupported path type. Please provide a valid file or directory.")
        return

    for _, wallet, _ in address_results:
        file_handler.write_output_to_file(extracted_addresses_filename, wallet)

    wallet_addresses = file_handler.read_wallet_addresses(extracted_addresses_filename)

    for wallet in wallet_addresses:
        address_type = address_extractor.identify_address_type(wallet)
        if address_type == "ETH" and check_eth:
            balance = eth.get_balance(wallet)
            process_balance(wallet, balance, final_output_filename)
        elif address_type == "BTC" and check_btc:
            balance = btc.get_balance(wallet)
            process_balance(wallet, balance, final_output_filename)
        elif address_type == "LTC" and check_ltc:
            balance = ltc.get_balance(wallet)
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