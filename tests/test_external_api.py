from unittest.mock import patch
from src.external_api import convert_to_rub


@patch("src.external_api.requests.get")
def test_convert_usd_to_rub(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 90.0}

    transaction = {"amount": "1", "currency": "USD"}
    result = convert_to_rub(transaction)
    assert result == 90.0


@patch("src.external_api.requests.get")
def test_convert_to_rub_error(mock_get):
    mock_get.return_value.status_code = 404

    transaction = {"amount": "1", "currency": "USD"}
    result = convert_to_rub(transaction)
    assert result == 0.0
