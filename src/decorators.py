import functools
import logging
from typing import Callable, Any


def log(filename: str | None = None) -> Callable:
    def decorator(func: Callable) -> Callable:
        logger = logging.getLogger(func.__name__)
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(message)s')

        if filename:
            handler = logging.FileHandler(filename)
        else:
            handler = logging.StreamHandler()

        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.propagate = False

        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            try:
                result = func(*args, **kwargs)
                logger.info(f"{func.__name__} ok")
                return result
            except Exception as e:
                logger.error(
                    f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                )
                raise

        return wrapper
    return decorator
