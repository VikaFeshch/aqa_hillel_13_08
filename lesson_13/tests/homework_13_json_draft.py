import logging
from pathlib import Path
import json

logging.basicConfig(
    filename='json_feshchenko.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
# logger = logging.getLogger("")

logger = logging.getLogger(__name__)

# Отримання списку всіх файлів
parent_dir = Path('../data/work_with_json')
files = [f for f in parent_dir.iterdir() if f.is_file()]

# Виведення списку всіх файлів
print("Список всіх файлів:")
for file in files:
    print("!!!!!!!!!!!!", file)

for f in parent_dir.iterdir():
    if f.is_file():
        with open(f, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
                print(f" $$$$$$$$$ {f} print {data}")
            except json.JSONDecodeError as e:
                print(f"Помилка розбору JSON у файлі {f}: {e}")
                logger.error(f"Помилка розбору JSON у файлі {f.name}: {e}")




