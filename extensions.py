import requests
import json
from config import keys


class APIException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}')
        try:
            qoute_ticker = keys[quote.lower()]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')
        try:
            base_ticker = keys[base.lower()]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={qoute_ticker}&tsyms={base_ticker}')
        total_base = round(float(json.loads(r.content)[base_ticker]) * amount, 2)
        return total_base
