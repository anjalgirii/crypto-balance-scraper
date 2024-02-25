import re

def identify_address_type(address):
    eth_pattern = "^0x[a-fA-F0-9]{40}$"
    btc_pattern = r"^(1[a-km-zA-HJ-NP-Z1-9]{25,34}|3[a-km-zA-HJ-NP-Z1-9]{33}|bc1[a-z0-9]{39,59})$"

    if re.match(eth_pattern, address):
        return "ETH"
    elif re.match(btc_pattern, address):
        return "BTC"
    else:
        return "UNKNOWN"
