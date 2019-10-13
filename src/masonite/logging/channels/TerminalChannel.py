import os

import pendulum
from masonite.helpers import config

from ..factory import DriverFactory
from ..channels.BaseChannel import BaseChannel


class TerminalChannel(BaseChannel):

    def __init__(self, driver=None, path=None):
        self.max_level = config('logging.channels.terminal.level', 'debug')
        self.driver = DriverFactory.make(driver or config('logging.channels.terminal.driver'))(path=path, max_level=self.max_level)
