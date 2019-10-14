from masonite.provider import ServiceProvider
from ..managers import LoggingManager
# from ..ChannelFactory import ChannelFactory
from ..factory import DriverFactory
from masonite.helpers import config
from ..Logger import Logger

class LoggingProvider(ServiceProvider):

    def register(self):
        self.app.bind('LogChannelFactory', ChannelFactory)
        self.app.bind('LogDriverFactory', DriverFactory)
        self.app.bind('LoggingManager', LoggingManager(ChannelFactory, DriverFactory))

    def boot(self, logging: LoggingManager):
        channel = logging.channel(config('logging.default'))

        self.app.bind('Logger', channel)
        self.app.swap(Logger, channel)
