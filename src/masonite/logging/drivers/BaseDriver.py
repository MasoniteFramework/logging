import pendulum
from masonite.helpers import config

class BaseDriver:

    levels = [
        'emergency'
        'alert'
        'critical'
        'error'
        'warning'
        'notice'
        'info'
        'debug'
    ]

    def get_time(self):
        return pendulum.now().in_tz(config('logging.channels.timezone', 'UTC'))

    def should_run(self, level, bubble=True):
        if self.levels.index()
    