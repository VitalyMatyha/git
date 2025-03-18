def get_mask_card_number(card_number: int) -> str:
    """Возвращает маску номера счета в формате XXXX XX** **** XXXX"""
    # Преобразуем номер карты в строку
    card_str = str(card_number)
    # Проверяем, достаточно ли длинный номер
    if len(card_str) == 16 and card_str.isdigit():
        # Создаем маску, оставляя видимыми только последние 4 цифры
        masked_card = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[12:]}"
        return masked_card
    else:
        return "Ошибка"
print("Maestro", get_mask_card_number(1596837868705199))
print("Visa Classic", get_mask_card_number(6831982476737658))
print("MasterCard ", get_mask_card_number(7158300734726758))

def get_mask_account(account_number: int) -> str:
    """озвращает маску номера счета в формате **XXXX"""
    account_str = str(account_number)
    if len(account_str) == 20 and account_str.isdigit():
        # Создаем маску, оставляя видимыми только последние 4 цифры
        masked_card = f"**{account_str[-4:]}"
        return masked_card
    else:
        return "Ошибка"
print(get_mask_account(35383033474447895560))
print(get_mask_account(64686473678894779589))
print(get_mask_account(73654108430135874305))
from datetime import datetime

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
