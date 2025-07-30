import logging
import logging.config
import inspect
from datetime import datetime

def custom_logger(loglevel=logging.DEBUG):
    now = datetime.now()
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)

    logger.setLevel(logging.DEBUG)
    fileHandler = logging.FileHandler('{0}'.format(loggerName)+'_'+str(now.strftime("%Y%m%d%H%M%S%p"))+'.log', mode='w')
    fileHandler.setLevel(loglevel)

    formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s:%(message)s', datefmt='%m/%d/%Y%I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger