import pendulum
from masonite.helpers import config

class BaseChannel:

    def get_time(self):
        
        return pendulum.now().in_tz(config('logging.channels.timezone', 'UTC'))
