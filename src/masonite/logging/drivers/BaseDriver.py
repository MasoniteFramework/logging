import pendulum
from masonite.helpers import config

class BaseDriver:

    def get_time(self):
        return pendulum.now().in_tz(config('logging.channels.timezone', 'UTC'))
