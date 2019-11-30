from datetime import datetime
import logging
import logging.config
import os
import sys

def start_logger(config_path:str = None):
    if config_path == None:
        config_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                    '..',
                                    'configurations',
                                    'logger.conf')
    logfilename = {'logfilename': 'log_{:%Y_%m_%d-%H_%M_%S}.txt'.format(datetime.now())}
    logging.config.fileConfig(config_path, defaults=logfilename)
    logger = logging.getLogger('logtool')
    
    return logger
