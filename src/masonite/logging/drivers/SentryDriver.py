from masonite.exceptions import DriverLibraryNotFound
from masonite.drivers import BaseDriver
from masonite.request import Request
from masonite import env

class SentryDriver(BaseDriver):

    def __init__(self):
        try:
            import sentry_sdk
        except ImportError:
            raise DriverLibraryNotFound(
                "No Sentry library found. Please install it by running 'pip install sentry-sdk'"
            )

        sentry_sdk.init(env('SENTRY_URL'))

    def exception(self, exception, request: Request):
        from sentry_sdk import capture_exception
        self.scopes(request)
        capture_exception(exception)
        
    def log(self, message):
        from sentry_sdk import capture_message
        capture_message(message)
        
    def scopes(self, request):
        from sentry_sdk import configure_scope

        with configure_scope() as scope:
            if request.user():
                scope.user = request.user().serialize()

            import masonite
            scope.set_tag("masonite_version", masonite.__version__)
