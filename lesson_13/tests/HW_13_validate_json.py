import logging
from pathlib import Path
import json

logging.basicConfig(
    filename='json_feshchenko.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("")

# get files from the dir
parent_dir = Path('../data/work_with_json')
files = [f for f in parent_dir.iterdir() if f.is_file()]

# checking json file
for f in parent_dir.iterdir():
    if f.is_file():
        with open(f, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError as e:
                logger.error(f"JSON parsing error in the file {f.name}: {e}")
