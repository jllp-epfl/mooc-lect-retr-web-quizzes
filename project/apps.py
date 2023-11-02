from django.apps import AppConfig
import os
import logging


class MyAppConfig(AppConfig):
    name = 'project'


    def ready(self):

        if os.environ.get('RUN_MAIN'):
            logger = logging.getLogger(__name__)
            # logger.propagate = False

            # Create a logger
            logger.setLevel(logging.DEBUG)

            # Create a file handler
            fh = logging.FileHandler('mylog.log')
            fh.setLevel(logging.DEBUG)

            # Create a console handler
            ch = logging.StreamHandler()
            ch.setLevel(logging.ERROR)

            # Create a formatter
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            # Add handlers to the logger
            logger.addHandler(fh)
            logger.addHandler(ch)

            # put your startup code here
            logger.debug('starting!')

