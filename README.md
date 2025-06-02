# 📦 Проект: Data Processing Module

## 📘 Описание

Этот проект представляет собой модуль для обработки банковских транзакций. В нём реализованы:

- Генераторы для работы с транзакциями.
- Декоратор логирования выполнения функций.
- Загрузка и обработка данных из JSON-файлов.
- Конвертация валют с использованием внешнего API.
- Поддержка переменных окружения через `.env`.
- Покрытие тестами с использованием `pytest`, `mock`, `patch`.

---

## 🚀 Установка

## 📄 Поддержка форматов CSV и Excel

Проект поддерживает загрузку финансовых транзакций из файлов форматов:

- JSON
- CSV
- Excel (.xlsx)

Функции `read_transactions_from_csv()` и `read_transactions_from_excel()` позволяют считывать данные и преобразовывать их в список словарей.

```bash
git clone https://github.com/VitalyMatyha/git.git
cd git
python -m venv venv
source venv/bin/activate  # для Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # создайте свой .env файл и укажите API ключ

