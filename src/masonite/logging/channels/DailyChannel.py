from ..factory import DriverFactory
from masonite.helpers import config
from masonite.helpers.filesystem import make_directory
import os
from .BaseChannel import BaseChannel

class DailyChannel(BaseChannel):

    def __init__(self, driver=None, path=None):
        path = path or config('logging.channels.daily.path')
        path = os.path.join(path, self.get_time().to_date_string() + '.log')
        self.max_level = config('logging.channels.daily.level')
        make_directory(path)
        self.driver = DriverFactory.make(driver or config('logging.channels.daily.driver'))(path=path, max_level=self.max_level)

    def debug(self, message, *args, **kwargs):
        return self.driver.debug(message, *args, **kwargs)