import re

def identify_address_type(address):
    # Ethereum (ETH) address regex pattern
    eth_pattern = "^0x[a-fA-F0-9]{40}$"


    if re.match(eth_pattern, address):
        return "ETH"  # Ethereum address
    else:
        return "UNKNOWN"  # Unknown address type

