
from ..factory import DriverFactory
from masonite.helpers import config
from masonite.helpers.filesystem import make_directory
import os
import pendulum
from .BaseChannel import BaseChannel

class SlackChannel(BaseChannel):

    def __init__(self, driver=None, path=None):
        token = config('logging.channels.slack.token')
        channel = config('logging.channels.slack.channel')
        emoji = config('logging.channels.slack.emoji')
        username = config('logging.channels.slack.username')
        self.max_level = config('logging.channels.slack.level')
        self.driver = DriverFactory.make(driver or config('logging.channels.slack.driver'))(emoji=emoji, username=username, token=token, channel=channel)

    def debug(self, message, *args, **kwargs):
        return self.driver.debug(message, *args, **kwargs)