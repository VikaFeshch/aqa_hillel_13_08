import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.StreamHandler(),  # log in console
                        logging.FileHandler('basic_example.log')  # in file
                    ])

logger = logging.getLogger(__name__)