from src.utils import read_json_file


def test_valid_json_file(tmp_path):
    file_path = tmp_path / "test.json"
    file_path.write_text('[{"amount": "100", "currency": "USD"}]', encoding="utf-8")

    result = read_json_file(str(file_path))
    assert isinstance(result, list)
    assert result[0]["amount"] == "100"


def test_invalid_json_file(tmp_path):
    file_path = tmp_path / "invalid.json"
    file_path.write_text('{"amount": "100"}', encoding="utf-8")  # Не список

    result = read_json_file(str(file_path))
    assert result == []


def test_file_not_found():
    result = read_json_file("data/not_exist.json")
    assert result == []
