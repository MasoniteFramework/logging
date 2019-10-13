from masonite import env
from masonite.environment import LoadEnvironment

LoadEnvironment()

DEFAULT='single'

CHANNELS = {
    'timezone': 'UTC',
    'single': {
        'driver': 'single',
        'level': 'debug',
        'path': 'storage/logs/single.log'
    },
    'stack': {
        'driver': 'stack',
        'channels': ['single', 'slack', 'daily']
    },
    'daily': {
        'driver': 'daily',
        'level': 'debug',
        'path': 'storage/logs'
    },
    'terminal': {
        'driver': 'terminal',
        'level': 'info',
    },
    'slack': {
        'driver': 'slack',
        'channel': '#bot',
        'emoji': ':warning:',
        'username': 'Logging Bot',
        'token': env('SLACK_TOKEN'),
        'level': 'debug'
    },
    'syslog': {
        'driver': 'syslog',
        'path': '/var/run/syslog',
        'level': 'debug'
    }
}