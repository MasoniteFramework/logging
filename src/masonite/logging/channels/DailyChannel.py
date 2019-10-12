from ..factory import DriverFactory
from masonite.helpers import config
from masonite.helpers.filesystem import make_directory
import os
import pendulum
from .BaseChannel import BaseChannel

class DailyChannel(BaseChannel):

    def __init__(self, driver=None, path=None):
        path = path or config('logging.channels.daily.path')
        import pendulum
        path = os.path.join(path, self.get_time().to_date_string() + '.log')
        make_directory(path)
        print('path is', path)
        self.driver = DriverFactory.make(driver or config('logging.channels.daily.driver'))(path=path)

    def debug(self, message, *args, **kwargs):
        return self.driver.debug(message, *args, **kwargs)