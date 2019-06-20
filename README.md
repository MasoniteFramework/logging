# Masonite Logging Package

This logging package will allow you to connect services like Sentry, Rollbar, and PaperTrail to send logging messages and exceptions for your application.

# Installation

To install the package you can use pip:

```
$ pip install masonite-logging
```

And add the provider to your `PROVIDERS` list:

```python
from masonite.logging.providers import LoggingProvider

PROVIDERS = [
    ..
    # Application Providers
    LoggingProvider,
]
```

Finally just run the public command:

```
$ craft publish LoggingProvider
```

This will add a new configuration to your `config/` directory.

# Using The Package

Inside your `config/logging.py` file you will find a few options:

```python
DRIVER = 'sentry'

DRIVERS = {
    'sentry': {
        'client': '',
        'secret': '',
    }
}
```
# Channels 

Masonite logging has the concept of channels which are similiar to database connections. You can have several channels and each channel can have it's own driver. For example you may have a `production` and `beta` channel.

# Stack Driver

You can also use a stack driver that will take several drivers. This will be useful if you want to log to several drivers like the local `disk` and `sentry` driver.

```python
DRIVER = 'stack'

DRIVERS = {
    'channels': {
        'stack': {
            'driver': 'stack',
            'channels': [
                'disk', 
                'sentry'
            ]
        }
        'sentry': {
            'driver': 'sentry',
            'client': '',
            'secret': '',
        }
    },
}
```

Channel names can be whatever you like them to be.

Now when an exception or message is logged it will log to both the disk and the sentry driver.

# Using the package

## Logging Messages

You can use the package in a few ways. The first way is to log a message:

```python
from masonite.logging import Logging

def show(self, logging: Logging):
    logging.message('hello world', severity='debug')
```

You have a few options for methods: `emergency`, `alert`, `critical`, `error`, `warning`, `notice`, `info`, and `debug`. You can also use these methods directly:

```python
from masonite.logging import Logging

def show(self, logging: Logging):
    logging.debug('hello world')
    logging.warning('hello world')
    logging.info('hello world')
    logging.emergency('hello world')
```

## Logging exceptions

Whenever an exception is encountered, Masonite will send the exeption to a logger's `exception` method. This will then send the information to the system that requires it.

You can optionally send this manually if you want:

```python
from masonite.logging import Logging

def show(self, logging: Logging):
    try:
        some_code()
    except Exception as e:
        logging.exception(e)
        raise e
```