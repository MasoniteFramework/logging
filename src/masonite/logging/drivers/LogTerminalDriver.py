# from logging import Logger
import os

from masonite.helpers import config, HasColoredCommands

from .BaseDriver import BaseDriver


class LogTerminalDriver(BaseDriver, HasColoredCommands):

    def __init__(self, *args, **kwargs):
        self.max_level=kwargs.get('max_level', None)
        self.bubble=kwargs.get('bubble', None)

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
        if not self.should_run('debug', self.max_level):
            return

        super().warning('{time} - {level} - {message}'.format(
            time=self.get_time().to_datetime_string(),
            level='DEBUG',
            message=message
        ))
