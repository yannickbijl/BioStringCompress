import logging
import logging.config

logging.config.fileConfig('configurations/logger.conf')
logger = logging.getLogger('logtool')
