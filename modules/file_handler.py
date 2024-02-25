def read_wallet_addresses(file_path):
    wallet_addresses = []
    try:
        with open(file_path, 'r') as file:
            wallet_addresses = file.read().split()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return wallet_addresses


def write_output_to_file(file_path, output):
    try:
        with open(file_path, 'a') as file:
            file.write(output + '\n')
    except FileNotFoundError:
        print(f"File not found: {file_path}")
