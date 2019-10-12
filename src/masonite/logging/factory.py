from .drivers import LogSingleDriver, LogTerminalDriver

class DriverFactory:

    drivers = {
        'single': LogSingleDriver,
        'daily': LogSingleDriver,
        'terminal': LogTerminalDriver
    }

    @classmethod
    def make(cls, driver):
        return cls.drivers.get(driver)
