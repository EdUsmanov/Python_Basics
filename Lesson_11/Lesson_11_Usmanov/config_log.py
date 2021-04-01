
import sys
import os
import logging
import logging.handlers

sys.path.append('../')

LOGGER = logging.getLogger('app.main')

FILE_HANDLER = logging.FileHandler('app.log', encoding='utf-8')
FILE_HANDLER.setLevel(logging.DEBUG)

FORMATTER = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

FILE_HANDLER.setFormatter(FORMATTER)

LOGGER.addHandler(FILE_HANDLER)
LOGGER.setLevel(logging.DEBUG)

if __name__ == '__main__':
    LOGGER.debug('Отладочная информация')
