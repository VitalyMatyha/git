import re
from typing import List, Dict

def search_transactions_by_description(transactions: List[Dict], keyword: str) -> List[Dict]:
    """
    Ищет транзакции, содержащие заданное слово в описании (регистронезависимо).

    Args:
        transactions: Список транзакций.
        keyword: Ключевое слово для поиска.

    Returns:
        Список транзакций, удовлетворяющих критерию поиска.
    """
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    return [tx for tx in transactions if pattern.search(tx.get("description", ""))]

from collections import Counter


def count_transaction_categories(transactions: List[Dict]) -> Dict[str, int]:
    """
    Подсчитывает количество транзакций по их описанию.

    :param transactions: Список транзакций
    :return: Словарь с описаниями как ключами и количеством вхождений как значениями
    """
    descriptions = [tx.get("description", "").strip() for tx in transactions]
    return dict(Counter(descriptions))
