from src.masks import get_mask_account
from src.masks import get_mask_card_number
from src.processing import sort_by_date

print(sort_by_date(
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
))
print(get_mask_card_number(1934567386528468))
print(get_mask_account(1934567386528468))

from src.utils import read_json_file
from src.file_readers import read_transactions_from_csv
from src.file_readers import read_transactions_from_excel
from src.processing import filter_by_state, filter_by_currency, sort_by_date
from src.search import search_transactions_by_description, count_transaction_categories


def main() -> None:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите источник данных:")
    print("1. JSON\n2. CSV\n3. Excel")

    data_source = input("Ваш выбор: ").strip()
    file_path = ""

    if data_source == "1":
        file_path = input("Введите путь к JSON-файлу: ")
        transactions = read_json_file(file_path)
    elif data_source == "2":
        file_path = input("Введите путь к CSV-файлу: ")
        transactions = read_transactions_from_csv(file_path)
    elif data_source == "3":
        file_path = input("Введите путь к Excel-файлу: ")
        transactions = read_transactions_from_excel(file_path)
    else:
        print("Некорректный ввод.")
        return

    # Ввод и фильтрация по статусу
    valid_statuses = {"EXECUTED", "CANCELED", "PENDING"}
    while True:
        status = input("Введите статус для фильтрации (EXECUTED, CANCELED, PENDING): ").upper()
        if status in valid_statuses:
            break
        print(f"Статус '{status}' недоступен. Попробуйте снова.")

    transactions = filter_by_state(transactions, status)

    if not transactions:
        print("Не найдено ни одной транзакции с указанным статусом.")
        return

    # Сортировка
    if input("Отсортировать операции по дате? (Да/Нет): ").lower() == "да":
        order = input("По возрастанию или по убыванию? ").lower()
        reverse = order == "по убыванию"
        transactions = sort_by_date(transactions, reverse=reverse)

    # Валюта
    if input("Выводить только рублевые транзакции? (Да/Нет): ").lower() == "да":
        transactions = filter_by_currency(transactions, "RUB")

    # Поиск по описанию
    if input("Отфильтровать по слову в описании? (Да/Нет): ").lower() == "да":
        keyword = input("Введите слово: ")
        transactions = search_transactions_by_description(transactions, keyword)

    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под условия.")
        return

    print(f"\nВсего банковских операций в выборке: {len(transactions)}\n")
    for tx in transactions:
        date = tx.get("date", "")[:10]
        description = tx.get("description", "")
        from_account = tx.get("from", "")
        to_account = tx.get("to", "")
        amount = tx["operationAmount"]["amount"]
        currency = tx["operationAmount"]["currency"]["name"]
        print(f"{date} {description}\n{from_account} -> {to_account}\nСумма: {amount} {currency}\n")

