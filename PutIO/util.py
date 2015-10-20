import requests
from urllib import urlencode
from urlparse import parse_qs, urlsplit, urlunsplit


def set_query_parameter(url, param_name, param_value):
    scheme, netloc, path, query_string, fragment = urlsplit(url)
    query_params = parse_qs(query_string)
    query_params[param_name] = [param_value]
    new_query_string = urlencode(query_params, doseq=True)
    return urlunsplit((scheme, netloc, path, new_query_string, fragment))


def urljoin(*args):
    return '/'.join(map(lambda x: str(x).rstrip('/'), args)).rstrip('/')


def request(url, method='get', **kwargs):
    return getattr(requests, method)(url, **kwargs)


def implode(data):
    return ','.join(map(lambda x: x, data))
