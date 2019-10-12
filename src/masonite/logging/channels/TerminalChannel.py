import os

import pendulum
from masonite.helpers import config

from ..factory import DriverFactory


class TerminalChannel:

    def __init__(self, driver=None, path=None):
        self.driver = DriverFactory.make(driver or config('logging.channels.terminal.driver'))(path=path)

    def debug(self, message, *args, **kwargs):
        return self.driver.debug(message, *args, **kwargs)
