import requests
from bs4 import BeautifulSoup
import json

def get_balance(wallet_address):
    config_file = 'config/config.json'
    
    with open(config_file, 'r') as file:
        config = json.load(file)
    
    btc_config = config.get("btc_config")
    
    if btc_config:
        scrape_site_url = btc_config.get("scrape_site_url")
        url = f"http://{scrape_site_url}/address/{wallet_address}"
        
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                tbody = soup.find('tbody')
                if tbody:
                    rows = tbody.find_all('tr')
                    for row in rows:
                        cells = row.find_all('td')
                        if cells and "Final Balance" in cells[0].text:
                            final_balance_span = cells[1].find('span', class_='prim-amt')
                            if final_balance_span:
                                balance_amount = final_balance_span.text.strip()
                                if " BTC" not in balance_amount:
                                    balance_amount += " BTC"
                                return balance_amount
                return "0 BTC"
            else:
                return "Error: Unable to fetch balance"
        except requests.exceptions.RequestException as e:
            print(f"Error fetching BTC balance: {e}")
            return "Error: Request Exception"
    else:
        print("BTC configuration not found in the config file.")
        return "Error: Config Not Found"
