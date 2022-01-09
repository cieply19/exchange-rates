import requests
from bs4 import BeautifulSoup
import csv, datetime, os
from django.conf import settings
from decimal import Decimal
from rates.models import Rate

response = requests.get("https://e-kursy-walut.pl/")
soup = BeautifulSoup(response.text, 'html.parser')

cryptos = (
    'Chainlink', 'Bitcoin', 'Ethereum', 'Cardano', 'Binance Coin', 'Solana', 'BitTorrent', 'Ripple', 'Litecoin', 'Iota')

rows = []
filepath = os.path.join(
    settings.FIXTURES_DIR, 'tmp_rates.csv'
)


def get_data():
    from decimal import Decimal
    for x in cryptos:
        if not soup.find(text=x):
            continue
        else:
            usd_rate = soup.find(text=x).next_element.small.text
            usd_rate = usd_rate.replace(' ', '')
            usd_rate = Decimal(usd_rate[0:len(usd_rate)-3])
            pln_rate = soup.find(text=x).next_element.strong.text
            pln_rate = pln_rate.replace(' ', '')
            pln_rate = Decimal(pln_rate[0:len(pln_rate)-3])

            rows.append({'Name': x, 'USD rate': usd_rate, 'PLN rate': pln_rate,
                         'Data + Time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})

    return rows


def create_csv():
    get_data()

    with open(filepath, 'w', newline='') as csvfile:
        csvwriter = csv.DictWriter(csvfile, ('Name', 'USD rate', 'PLN rate', 'Data + Time'))
        if not csvfile.tell():
            csvwriter.writeheader()

        csvwriter.writerows(rows)
