from typing import Dict
from typing import List

import pandas as pd


def read_transactions_from_csv(transactions: str) -> List[Dict]:
    """
    Читает CSV-файл и возвращает список транзакций.

    Args:
        filepath (str): Путь к CSV-файлу.

    Returns:
        List[Dict]: Список транзакций.
    """
    try:
        df = pd.read_csv(transactions)
        return df.to_dict(orient="records")
    except Exception as e:
        return []


def read_transactions_from_excel(transactions_excel: str) -> List[Dict]:
    """
    Читает Excel-файл и возвращает список транзакций.

    Args:
        filepath (str): Путь к Excel-файлу (.xlsx).

    Returns:
        List[Dict]: Список транзакций.
    """
    try:
        df = pd.read_excel(transactions_excel)
        return df.to_dict(orient="records")
    except Exception as e:
        return []
