import logging

import pytest

from src.decorators import log


def test_log_success_console(caplog):
    @log()
    def add(x, y):
        return x + y

    with caplog.at_level(logging.INFO):
        result = add(1, 2)

    assert "add ok" in caplog.text
    assert result == 3


def test_log_error_console(caplog):
    @log()
    def fail(x):
        raise ValueError("Test error")

    with caplog.at_level(logging.ERROR):
        with pytest.raises(ValueError):
            fail(1)

    assert "fail error: ValueError" in caplog.text
    assert "Inputs: (1,)" in caplog.text
