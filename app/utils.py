import os
import logging


logger = logging.getLogger('TodoListLogger')
logger.setLevel(os.environ.get('LOGGER_LEVEL', logging.WARNING))
