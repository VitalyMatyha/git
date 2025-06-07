import pytest
from src.search import search_transactions_by_description, count_transaction_categories

MOCK_TRANSACTIONS = [
    {"description": "Оплата телефона"},
    {"description": "Перевод другу"},
    {"description": "Оплата телефона"},
    {"description": "Снятие наличных"},
]

def test_search_by_description_found():
    result = search_transactions_by_description(MOCK_TRANSACTIONS, "телефон")
    assert len(result) == 2

def test_search_by_description_not_found():
    result = search_transactions_by_description(MOCK_TRANSACTIONS, "магазин")
    assert result == []

def test_count_transaction_categories():
    result = count_transaction_categories(MOCK_TRANSACTIONS)
    assert result["Оплата телефона"] == 2
    assert result["Перевод другу"] == 1
