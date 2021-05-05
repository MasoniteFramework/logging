import logging
import os
from .BaseDriver import BaseDriver

class LogSingleDriver(BaseDriver):

    def __init__(self, *args, **kwargs):
        self.max_level = kwargs.get('max_level')
        self.path = kwargs.get('path')
        self.log = logging.getLogger('root')

        handler = logging.FileHandler(self.path, 'a')
        formatter = logging.Formatter('{} - %(levelname)s - %(message)s'.format(self.get_time().to_datetime_string()))
        
        handler.setFormatter(formatter)
        self.log.addHandler(handler)

    def change_format(self, changed_format):
        for hdlr in self.log.handlers[:]:  # remove all old handlers
            self.log.removeHandler(hdlr)

        handler = logging.FileHandler(self.path, 'a')
        formatter = logging.Formatter(changed_format)
        
        handler.setFormatter(formatter)

        self.log.addHandler(handler)

    def emergency(self, message, *args, **kwargs):
        self.log.setLevel(logging.CRITICAL)
        self.change_format('{} - {} - %(message)s'.format(
                self.get_time().to_datetime_string(),
                'EMERGENCY'))
        return self.log.critical(message, *args, **kwargs)

    def alert(self, message, *args, **kwargs):
        self.log.setLevel(logging.CRITICAL)
        self.change_format('{} - {} - %(message)s'.format(
                self.get_time().to_datetime_string(),
                'ALERT'))
        return self.log.critical(message, *args, **kwargs)

    def critical(self, message, *args, **kwargs):
        self.log.setLevel(logging.CRITICAL)
        self.change_format('{} - {} - %(message)s'.format(
            self.get_time().to_datetime_string(),
            'CRITICAL'))
        return self.log.critical(message, *args, **kwargs)

    def error(self, message, *args, **kwargs):
        self.log.setLevel(logging.ERROR)
        self.change_format('{} - {} - %(message)s'.format(
            self.get_time().to_datetime_string(),
            'ERROR'))
        return self.log.error(message, *args, **kwargs)

    def warning(self, message, *args, **kwargs):
        self.log.setLevel(logging.WARNING)
        self.change_format('{} - {} - %(message)s'.format(
            self.get_time().to_datetime_string(),
            'WARNING'))
        return self.log.warning(message, *args, **kwargs)

    def notice(self, message, *args, **kwargs):
        self.log.setLevel(logging.INFO)
        self.change_format('{} - {} - %(message)s'.format(
            self.get_time().to_datetime_string(),
            'NOTICE'))
        return self.log.info(message, *args, **kwargs)

    def info(self, message, *args, **kwargs):
        self.log.setLevel(logging.INFO)
        self.change_format('{} - {} - %(message)s'.format(
            self.get_time().to_datetime_string(),
            'INFO'))
        return self.log.info(message, *args, **kwargs)

    def debug(self, message, *args, **kwargs):
        self.log.setLevel(logging.DEBUG)
        self.change_format('{} - {} - %(message)s'.format(
            self.get_time().to_datetime_string(),
            'DEBUG'))
        return self.log.debug(message, *args, **kwargs) 
    