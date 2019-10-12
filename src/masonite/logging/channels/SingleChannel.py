from ..factory import DriverFactory
from masonite.helpers import config
from masonite.helpers.filesystem import make_directory
import os
import pendulum

class SingleChannel:

    def __init__(self, driver=None, path=None):
        path = path or config('logging.channels.single.path')
        make_directory(path)
        print('path is', path)
        self.driver = DriverFactory.make(driver or config('logging.channels.single.driver'))(path=path)

    def debug(self, message, *args, **kwargs):
        return self.driver.debug(message, *args, **kwargs)