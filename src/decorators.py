import logging
from functools import wraps
from typing import Any
from typing import Callable


def log(filename: str = None):
    """
    Декоратор логирует выполнение функции. Принимает необязательный аргумент `filename`.
    Если указан, лог записывается в файл. Если не указан — выводится в консоль.
    Лог содержит имя функции, успешный результат или информацию об ошибке с входными параметрами.
    """

    def decorator(func: Callable) -> Callable:
        logger = logging.getLogger(func.__name__)
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter("%(message)s")

        if filename:
            handler = logging.FileHandler(filename)
        else:
            handler = logging.StreamHandler()

        handler.setFormatter(formatter)
        logger.handlers = [handler]

        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            try:
                result = func(*args, **kwargs)
                logger.info(f"{func.__name__} ok")
                return result
            except Exception as e:
                logger.error(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                raise

        return wrapper

    return decorator
