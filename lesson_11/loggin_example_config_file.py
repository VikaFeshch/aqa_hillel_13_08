import logging
import logging.config

logging.config.fileConfig('logging_config.ini')
logger = logging.getLogger('sampleLogger')

logger.debug('message DEBUG')
logger.info('message INFO')
logger.warning('message WARNING')
logger.error('message ERROR')
logger.critical('message CRITICAL')