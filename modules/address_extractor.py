import os
import re

def identify_address_type(address):
    eth_pattern = "^0x[a-fA-F0-9]{40}$"
    btc_pattern = r"^(1[a-km-zA-HJ-NP-Z1-9]{25,34}|3[a-km-zA-HJ-NP-Z1-9]{33}|bc1[a-z0-9]{39,59})$"
    ltc_pattern = r"^(L[a-zA-Z0-9]{33}|M[a-zA-Z0-9]{33}|ltc1[a-z0-9]{39,59})$"
    if re.match(eth_pattern, address):
        return "ETH"
    elif re.match(btc_pattern, address):
        return "BTC"
    elif re.match(ltc_pattern, address):
        return "LTC"
    return "UNKNOWN"

def walk_and_extract_addresses(root_dir):
    result_list = []
    address_pattern = r"(0x[a-fA-F0-9]{40})|(1[a-km-zA-HJ-NP-Z1-9]{25,34}|3[a-km-zA-HJ-NP-Z1-9]{33}|bc1[a-z0-9]{39,59})|(L[a-zA-Z0-9]{33}|M[a-zA-Z0-9]{33}|ltc1[a-z0-9]{39,59})"
    for root, _, files in os.walk(root_dir):
        for filename in files:
            file_path = os.path.join(root, filename)
            if filename.endswith(('.ldb', '.log', '.txt')):
                result_list.extend(process_file(file_path, address_pattern))
    return result_list

def extract_addresses_from_file(file_path):
    address_pattern = r"(0x[a-fA-F0-9]{40})|(1[a-km-zA-HJ-NP-Z1-9]{25,34}|3[a-km-zA-HJ-NP-Z1-9]{33}|bc1[a-z0-9]{39,59})|(L[a-zA-Z0-9]{33}|M[a-zA-Z0-9]{33}|ltc1[a-z0-9]{39,59})"
    return process_file(file_path, address_pattern)

def process_file(file_path, address_pattern):
    result_list = []
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            data = file.read()
            potential_addresses = re.findall(address_pattern, data)
            for address_group in potential_addresses:
                for address in address_group:
                    if address:
                        address_type = identify_address_type(address)
                        if address_type != "UNKNOWN":
                            result_list.append((file_path, address, address_type))
    except Exception as err:
        print(f"Error processing {file_path}: {err}")
    return result_list