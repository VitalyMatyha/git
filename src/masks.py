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


def get_mask_account(account_number: int) -> str:
    """озвращает маску номера счета в формате **XXXX"""
    account_str = str(account_number)
    if len(account_str) == 16 and account_str.isdigit():
        # Создаем маску, оставляя видимыми только последние 4 цифры
        masked_card = f"**{account_str[-4:]}"
        return masked_card
    else:
        return "Ошибка"
