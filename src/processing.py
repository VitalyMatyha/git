from typing import List, Dict
from datetime import datetime


def filter_by_state(data: List[Dict], state: str) -> List[Dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param data: Список операций (словарей).
    :param state: Желаемое состояние (например, 'EXECUTED').
    :return: Отфильтрованный список.
    """
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по дате.

    :param data: Список операций.
    :param reverse: True для убывания, False — для возрастания.
    :return: Отсортированный список.
    """
    def get_date(item):
        date_str = item.get("date")
        try:
            return datetime.fromisoformat(date_str)
        except (TypeError, ValueError):
            return datetime.min if reverse else datetime.max

    return sorted(data, key=get_date, reverse=reverse)
