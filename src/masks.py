import logging
import os

# Настройка логгера
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs', 'masks.log')
file_handler = logging.FileHandler(log_path, mode='w', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: int) -> str:
    """Возвращает маску номера карты в формате XXXX XX** **** XXXX"""
    card_str = str(card_number)
    if len(card_str) == 16 and card_str.isdigit():
        masked_card = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[12:]}"
        logger.debug(f"Маскирован номер карты: {masked_card}")
        return masked_card
    else:
        logger.error(f"Некорректный номер карты: {card_str}")
        return "Ошибка"


def get_mask_account(account_number: int) -> str:
    """Возвращает маску номера счета в формате **XXXX"""
    account_str = str(account_number)
    if len(account_str) == 20 and account_str.isdigit():
        masked_account = f"**{account_str[-4:]}"
        logger.debug(f"Маскирован номер счета: {masked_account}")
        return masked_account
    else:
        logger.error(f"Некорректный номер счета: {account_str}")
        return "Ошибка"
