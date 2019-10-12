# from logging import Logger
import os

from masonite.helpers import config, HasColoredCommands

from .BaseDriver import BaseDriver


class LogTerminalDriver(BaseDriver, HasColoredCommands):

    def __init__(self, path=None):
        # self.level = config('logging.channels.single.')
        # self.level = logging.DEBUG
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
        super().warning('{time} - {level} - {message}'.format(
            time=self.get_time().to_datetime_string(),
            level='DEBUG',
            message=message
        ))
