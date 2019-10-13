from ..factory import DriverFactory
from masonite.helpers import config
from masonite.helpers.filesystem import make_directory
import os
import pendulum
from .BaseChannel import BaseChannel

class SingleChannel(BaseChannel):

    def __init__(self, driver=None, path=None):
        path = path or config('logging.channels.single.path')
        make_directory(path)
        self.max_level = config('logging.channels.single.level')
        self.driver = DriverFactory.make(driver or config('logging.channels.single.driver'))(path=path, max_level=self.max_level)

"""
        'emergency',
        'alert',
        'critical',
        'error',
        'warning',
        'notice',
        'info',
        'debug',
"""