import logging
from src.utils.logger_util import logger

# Налаштування логування
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def logger_of_arg_resul(func):
    def wrapper(name):
        logging.info(f"Arguments of function '{func.__name__}': {name}")
        result = func(name)
        logging.info(f"Result of function '{func.__name__}': {result}")
        return result
    return wrapper

@logger_of_arg_resul
def say_hello(name):
    message = f"{name} says: 'Hello world'"
    print(message)
    return message  # Додаємо return, щоб повернути результат

# Виклик функції
say_hello("Vika")
