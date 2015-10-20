__title__ = 'python-putio'
__version__ = '0.1'
__api_ver__ = 'v2'
__api_link__ = 'https://api.put.io'

from .oauth_token import oauth_token

# Set default logging handler to avoid "No handler found" warnings.
import logging
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
