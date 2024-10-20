import logging

from src.utils.logger_util import logger

def exception_handler(func):
    def wrapper(a, b):
        try:
            return func(a, b)
        except Exception as e:
            logging.error(f"An error occurred in function '{func.__name__}': {e}")
            return None
    return wrapper


@exception_handler
def divide(a,b):
    result = a / b
    print(result)
    return result

divide(4, 0)

