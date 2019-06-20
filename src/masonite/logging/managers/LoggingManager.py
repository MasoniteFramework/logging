from masonite.managers import Manager

class LoggingManager(Manager):

    config = 'LoggingConfig'
    driver_prefix = 'Logging'