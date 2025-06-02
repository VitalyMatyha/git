import json
import logging
import os
from typing import List

# Настройка логгера
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "utils.log")
file_handler = logging.FileHandler(log_path, mode="w", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def read_json_file(filepath: str) -> List[dict]:
    """
    Читает JSON-файл и возвращает список транзакций.

    Args:
        filepath (str): Путь до JSON-файла.

    Returns:
        List[dict]: Список транзакций или пустой список.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.debug(f"Прочитано {len(data)} транзакций из файла: {filepath}")
                return data
            else:
                logger.error(f"Файл {filepath} не содержит список.")
    except FileNotFoundError:
        logger.error(f"Файл не найден: {filepath}")
    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON в файле: {filepath}")

    return []
