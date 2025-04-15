from src.widget import get_mask_account, get_date
import pytest

@pytest.mark.parametrize("input_data,expected", [
    ("40817810099910004312", "**4312"),
    ("1234567812345678", "1234 56** **** 5678"),
])
def test_mask_account_card(input_data, expected):
    assert get_mask_account(input_data) == expected

@pytest.mark.parametrize("date_str,expected", [
    ("2023-04-10T10:00:00", "10.04.2023"),
    ("", ""),
])
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected
