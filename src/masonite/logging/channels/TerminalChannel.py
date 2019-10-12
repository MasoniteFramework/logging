import os

import pendulum
from masonite.helpers import config

from ..factory import DriverFactory


class TerminalChannel:

    def __init__(self, driver=None, path=None):
        max_level = config('logging.channels.terminal.level', 'debug')
        bubble = config('logging.channels.terminal.bubble', True)
        self.driver = DriverFactory.make(driver or config('logging.channels.terminal.driver'))(path=path, max_level=max_level, bubble=bubble)

    def debug(self, message, *args, **kwargs):
        return self.driver.debug(message, *args, **kwargs)
