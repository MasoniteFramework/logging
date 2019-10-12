CHANNELS = {
    'timezone': 'UTC',
    'single': {
        'driver': 'single',
        'level': 'debug',
        'bubble': True,
        'path': 'storage/logs/single.log'
    },
    'daily': {
        'driver': 'daily',
        'level': 'debug',
        'bubble': True,
        'path': 'storage/logs'
    },
    'terminal': {
        'driver': 'terminal',
        'level': 'debug',
        'bubble': True,
    },
}