import requests

class CurrencyConverter:
    def __init__(self, api_url):
        self.api_url = api_url

    def get_exchange_rate(self, from_currency, to_currency):
        response = requests.get(f"{self.api_url}/latest/{from_currency}")
        data = response.json()
        return data['rates'][to_currency]

    def convert(self, amount, from_currency, to_currency):
        rate = self.get_exchange_rate(from_currency, to_currency)
        return amount * rate
