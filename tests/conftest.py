import pytest

@pytest.fixture
def card_numbers():
    return ["1234567812345678", "4111111111111111", ""]

@pytest.fixture
def account_numbers():
    return ["40817810099910004312", "123", ""]

@pytest.fixture
def operations_data():
    return [
        {"state": "EXECUTED", "date": "2023-01-01"},
        {"state": "CANCELED", "date": "2022-12-01"},
        {"state": "EXECUTED", "date": "2023-03-01"},
    ]
