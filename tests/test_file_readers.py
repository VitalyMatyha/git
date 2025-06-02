from unittest.mock import patch

import pandas as pd
import pytest

from src.file_readers import read_transactions_from_csv
from src.file_readers import read_transactions_from_excel


@patch("pandas.read_csv")
def test_read_transactions_from_csv(mock_read_csv):
    mock_read_csv.return_value = pd.DataFrame([{"amount": 100, "currency": "USD"}])
    result = read_transactions_from_csv("fake_path.csv")
    assert isinstance(result, list)
    assert result[0]["amount"] == 100


@patch("pandas.read_excel")
def test_read_transactions_from_excel(mock_read_excel):
    mock_read_excel.return_value = pd.DataFrame([{"amount": 200, "currency": "EUR"}])
    result = read_transactions_from_excel("fake_path.xlsx")
    assert isinstance(result, list)
    assert result[0]["currency"] == "EUR"
