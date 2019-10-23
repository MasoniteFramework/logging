from masonite.provider import ServiceProvider
from ..managers import LoggingManager
from ..ChannelFactory import ChannelFactory
from ..factory import DriverFactory
from masonite.helpers import config
from ..Logger import Logger
from ..listeners import LoggerExceptionListener

class LoggingProvider(ServiceProvider):

    wsgi = False
    
    def register(self):
        self.app.bind('LogChannelFactory', ChannelFactory)
        self.app.bind('LogDriverFactory', DriverFactory)
        self.app.bind('LoggingManager', LoggingManager(ChannelFactory, DriverFactory))
        self.app.simple(LoggerExceptionListener)
        config_path = os.path.join(os.path.dirname(__file__), '../configs')

        self.publishes({
            os.path.join(config_path, 'logging.py'): 'config/logging.py'
        }, tag="config")

    def boot(self, logging: LoggingManager):
        channel = logging.channel(config('logging.default'))

        self.app.bind('Logger', channel)
        self.app.swap(Logger, channel)
