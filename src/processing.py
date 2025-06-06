from typing import Dict
from typing import List


def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Фильтрует список операций по заданному статусу."""
    return [item for item in data if item.get("state") == state]


# data = [
#     {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
# ]
#
# print(filter_by_state(data))  # Фильтрация по умолчанию
# print(filter_by_state(data, "CANCELED"))  # Фильтрация по другому статусу


from datetime import datetime
from typing import Dict
from typing import List


def sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]:
    """Сортирует список операций по дате (по умолчанию — убывание)."""
    return sorted(data, key=lambda x: datetime.fromisoformat(x["date"]), reverse=reverse)


# data = [
#     {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
# ]
#
# print(sort_by_date(data))  # По убыванию
# print(sort_by_date(data, reverse=False))  # По возрастанию
