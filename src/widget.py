from datetime import datetime
from masks import get_mask_card_number, get_mask_account  # Импортируем функции из masks.py

# Используем импортированные функции
print("Maestro", get_mask_card_number(1596837868705199))
print("Visa Classic", get_mask_card_number(6831982476737658))
print("MasterCard", get_mask_card_number(7158300734726758))

print(get_mask_account(35383033474447895560))
print(get_mask_account(64686473678894779589))
print(get_mask_account(73654108430135874305))

def get_date(date_str: str) -> str:
    """
    Convert a date string from ISO format to the format DD.MM.YYYY.

    Args:
        date_str (str): The date string in ISO format (YYYY-MM-DDTHH:MM:SS.ssssss).

    Returns:
        str: The formatted date string in DD.MM.YYYY format.
    """
    try:
        # Преобразуем строку в объект datetime
        date_obj = datetime.fromisoformat(date_str)
        # Форматируем дату в нужный формат
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        return "Invalid date format. Please use the format YYYY-MM-DDTHH:MM:SS.ssssss."