from . import __api_ver__, __api_link__
from .url import url
from .util import set_query_parameter, urljoin


class base():
    def __init__(self, oauth_token=None):
        self.oauth_token = oauth_token

    def to_u(self, path=[], query={}, method='get'):
        _url = urljoin(
            urljoin(__api_link__, __api_ver__),
            self.__class__.__name__.lower()
        )
        for path_value in path:
            _url = urljoin(_url, path_value)
        for query_key, query_value in query.items():
            _url = set_query_parameter(_url, query_key, query_value)
        _url = set_query_parameter(_url, 'oauth_token', self.oauth_token)
        return url(url=_url)
