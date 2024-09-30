import logging
from pathlib import Path
import json

# Налаштування логування
logging.basicConfig(
    filename='login_system.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

# Отримання списку всіх файлів
parent_dir = Path('../data/work_with_json')
files = [f for f in parent_dir.iterdir() if f.is_file()]

# Виведення списку всіх файлів
logger.info("Список всіх файлів:")
for file in files:
    logger.info(f"Знайдено файл: {file}")

# Обробка кожного JSON-файлу
for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            data = json.load(file)
            logger.info(f"Успішно прочитано файл {f.name}: {data}")
    except json.JSONDecodeError as e:
        logger.error(f"Помилка розбору JSON у файлі {f.name}: {e}")
    except Exception as e:
        logger.error(f"Інша помилка при обробці файлу {f.name}: {e}")
