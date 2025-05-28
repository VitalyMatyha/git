import os
import requests
from typing import Dict
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("EXCHANGE_API_KEY")


def convert_to_rub(transaction: Dict) -> float:
    """Конвертирует сумму транзакции в рубли, если валюта USD или EUR.

    Args:
        transaction (dict): Транзакция с валютой и суммой.

    Returns:
        float: Сумма в рублях.
    """
    currency = transaction.get("currency")
    amount = float(transaction.get("amount", 0))

    if currency in ("USD", "EUR"):
        url = f"https://api.apilayer.com/exchangerates_data/convert"
        params = {
            "to": "RUB",
            "from": currency,
            "amount": amount
        }
        headers = {
            "apikey": API_KEY
        }

        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200:
            return response.json().get("result", 0.0)

        return 0.0

    return amount
