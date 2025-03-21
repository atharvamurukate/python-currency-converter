import matplotlib.pyplot as plt
import requests

class CurrencyGraph:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_historical_rates(self, from_currency, to_currency, days=30):
        response = requests.get(f"{self.api_url}/history/{from_currency}/{to_currency}?days={days}")
        data = response.json()
        return data['rates']

    def plot_graph(self, from_currency, to_currency):
        rates = self.fetch_historical_rates(from_currency, to_currency)
        dates = list(rates.keys())
        values = list(rates.values())

        plt.plot(dates, values)
        plt.xlabel('Date')
        plt.ylabel(f'Exchange Rate ({from_currency} to {to_currency})')
        plt.title(f'Historical Exchange Rates: {from_currency} to {to_currency}')
        plt.show()
