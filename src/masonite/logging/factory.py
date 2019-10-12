from .drivers import LogSingleDriver, LogTerminalDriver, LogSlackDriver

class DriverFactory:

    drivers = {
        'single': LogSingleDriver,
        'daily': LogSingleDriver,
        'slack': LogSlackDriver,
        'terminal': LogTerminalDriver
    }

    @classmethod
    def make(cls, driver):
        return cls.drivers.get(driver)
