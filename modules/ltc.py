import requests
import json
from bs4 import BeautifulSoup

def get_balance(wallet_address):
    config_file = 'config/config.json'

    with open(config_file, 'r') as config_file:
        config = json.load(config_file)

    coin_config = config.get(f"ltc_config")

    if coin_config:
        scrape_site_url = coin_config.get("scrape_site_url")
        url = f"http://{scrape_site_url}/address/{wallet_address}"

        try:
            response = requests.get(url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                target_table = soup.find('table', class_='table data-table')
                balance_amount = "Balance not found"  # Default message if balance is not found

                if target_table:
                    rows = target_table.find_all('tr')

                    for row in rows:
                        cells = row.find_all('td')
                        if cells and "Final Balance" in cells[0].text:
                            balance_amount = cells[1].text.strip()  # Extracting balance amount
                            break  

                return balance_amount
            else:
                return "Error: Response status code is not 200"
        except requests.exceptions.RequestException as e:
            return f"Error: {str(e)}"
    else:
        print("LTC configuration not found in the config file.")
        return "Configuration not found"