import os
import datetime
from modules import eth
from modules import file_handler
from modules import address_identifier


wallet_addresses = file_handler.read_wallet_addresses('wallets.txt')
current_date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
output_folder = os.path.join('output', current_date)
os.makedirs(output_folder, exist_ok=True)
log_filename = os.path.join(output_folder, 'output.log')
with_balance_filename = os.path.join(output_folder, 'with_balance.txt')

with open(log_filename, 'w') as output_log, open(with_balance_filename, 'w') as with_balance_file:
    for address in wallet_addresses:
        address_type = address_identifier.identify_address_type(address)
        coin_identifier = ""

        if address_type == "ETH":
            coin_identifier = "eth"

        if coin_identifier:
            balance = eth.get_balance(address, coin_identifier)

            output_message = f"{address_type}: {address}"

            if balance is not None:
                output_message += f" - Balance: {balance}"

            print(output_message)
            output_log.write(output_message + '\n')

            if "Balance: 0.00 USD" not in output_message:
                with_balance_file.write(output_message + '\n')

print("Processing completed. Results are saved in the 'output' folder.")
