import os

import pendulum
from masonite.helpers import config

from ..factory import DriverFactory


class TerminalChannel:

    def __init__(self, driver=None, path=None):
        self.max_level = config('logging.channels.terminal.level', 'debug')
        self.driver = DriverFactory.make(driver or config('logging.channels.terminal.driver'))(path=path, max_level=self.max_level)

    def debug(self, message, *args, **kwargs):
        return self.driver.debug(message, *args, **kwargs)
