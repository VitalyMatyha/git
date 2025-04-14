import pytest
from your_package.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize("card,expected", [
    ("1234567812345678", "1234 56** **** 5678"),
    ("", ""),
])
def test_get_mask_card_number(card, expected):
    assert get_mask_card_number(card) == expected

@pytest.mark.parametrize("account,expected", [
    ("40817810099910004312", "**4312"),
    ("123", "**123"),
])
def test_get_mask_account(account, expected):
    assert get_mask_account(account) == expected

