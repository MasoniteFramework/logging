from .drivers import LogSingleDriver

class DriverFactory:

    drivers = {
        'single': LogSingleDriver,
        'daily': LogSingleDriver,
    }

    @classmethod
    def make(cls, driver):
        return cls.drivers.get(driver)
