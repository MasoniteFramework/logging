# from logging import Logger
import logging
from masonite.helpers import config
import os
from .BaseDriver import BaseDriver

class LogSingleDriver(BaseDriver):

    def __init__(self, path=None):
        # self.level = config('logging.channels.single.')
        self.level = logging.DEBUG
        print(path)
        self.path = path

    def emergency(self, message):
        pass

    def alert(self, message):
        pass

    def critical(self, message):
        pass

    def error(self, message):
        pass

    def warning(self, message):
        pass

    def notice(self, message):
        pass

    def info(self, message):
        pass

    def debug(self, message):
        # import pendulum
        logging.basicConfig(
            level=self.level, 
            filename=os.path.join(self.path),
            format='{} - %(levelname)s - %(message)s'.format(self.get_time().to_datetime_string()))
        return logging.debug(message)
