import unittest
from src.masonite.logging.drivers import SentryDriver
from src.masonite.logging.managers import LoggingManager
from masonite.app import App
from masonite.request import Request
from masonite.environment import LoadEnvironment

LoadEnvironment()

class TestSentry(unittest.TestCase):

    def setUp(self):
        self.app = App()
        self.app.bind('Container', self.app)
        self.app.bind('Request', Request())
        self.app.bind('LoggingSentryDriver', SentryDriver)
        self.app.bind('LoggingManager', LoggingManager)
    
    def test_can_import(self):
        sentry = self.app.make('LoggingManager').driver('sentry')
        self.app.make('Request').set_user(MockUser())
        # sentry.log('hello world')
        try:
            return 2/0
        except Exception as e:
            self.app.resolve(sentry.exception, e)

class MockUser:

    def serialize(self):
        return {
            'email': 'joe@masoniteproject.com',
            'password': 'secret',
            'username': 'Joe',
            'active': 1
        }