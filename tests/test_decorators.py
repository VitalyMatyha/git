import pytest
import os
from src.decorators import log


def test_log_success_console(capsys):
    @log()
    def add(x, y):
        return x + y

    result = add(2, 3)
    assert result == 5
    captured = capsys.readouterr()
    assert "add ok" in captured.out


def test_log_error_console(capsys):
    @log()
    def fail(x):
        raise ValueError("fail")

    with pytest.raises(ValueError):
        fail(1)

    captured = capsys.readouterr()
    assert "fail error: ValueError" in captured.out
    assert "Inputs: (1,)" in captured.out


def test_log_to_file(tmp_path):
    log_file = tmp_path / "log.txt"

    @log(filename=str(log_file))
    def multiply(x, y):
        return x * y

    result = multiply(2, 4)
    assert result == 8

    content = log_file.read_text()
    assert "multiply ok" in content
