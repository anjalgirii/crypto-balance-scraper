import os
import re
from .address_identifier import identify_address_type  # Adjust import path as necessary

def walk_and_extract_addresses(root_dir):
    result_list = []

    # A more inclusive regex pattern to capture both ETH and BTC addresses; adjust as necessary for other types
    address_pattern = r"(0x[a-fA-F0-9]{40})|(1[a-km-zA-HJ-NP-Z1-9]{25,34}|3[a-km-zA-HJ-NP-Z1-9]{33}|bc1[a-z0-9]{39,59})"

    for root, _, files in os.walk(root_dir):
        for filename in files:
            if filename.endswith(('.ldb', '.log', '.txt')):  # Look for .ldb, .log, and .txt files
                file_path = os.path.join(root, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                        data = file.read()
                        potential_addresses = list(set(re.findall(address_pattern, data)))  # Extract potential addresses

                        for address_group in potential_addresses:
                            for address in address_group:
                                if address:  # Skip empty matches
                                    address_type = identify_address_type(address)
                                    if address_type != "UNKNOWN":  # Only add known address types
                                        result_list.append((file_path, address, address_type))
                except Exception as err:
                    print(f"Error processing {file_path}: {err}")

    return result_list