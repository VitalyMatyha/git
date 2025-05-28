from typing import List
import json


def read_json_file(filepath: str) -> List[dict]:
    """
    Читает JSON-файл и возвращает список транзакций.

    Args:
        filepath (str): Путь до JSON-файла.

    Returns:
        List[dict]: Список транзакций или пустой список.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []

    return []
