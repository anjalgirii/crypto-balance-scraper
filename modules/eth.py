import requests
from bs4 import BeautifulSoup
import json

def is_valid_wallet_address(address):
    return address.startswith('0x') and len(address) == 42

def get_balance(wallet_address):
    config_file = 'config/config.json'
    
    with open(config_file, 'r') as config_file:
        config = json.load(config_file)
    
    coin_config = config.get(f"eth_config")
    
    if coin_config:
        scrape_site_url = coin_config.get("scrape_site_url")
        url = f"http://{scrape_site_url}/address/{wallet_address}"
        
        try:
            response = requests.get(url)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                target_table = soup.find('table', class_='table data-table info-table')
                balance_amount = None
                
                if target_table:
                    rows = target_table.find_all('tr')
                    
                    for row in rows:
                        cell = row.find('td')
                        
                        if cell:
                            cell_text = cell.text.strip()
                            
                            if "Balance" in cell_text:
                                balance_row = row
                                balance_cell = balance_row.find_all('td')[1]
                                balance_amount = balance_cell.find('span', class_='sec-amt').text
                                break
                
                return balance_amount
            else:
                return None
        except requests.exceptions.RequestException as e:
            return None
    else:
        print("ETH configuration not found in the config file.")
        return None
