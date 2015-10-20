from .stream import stream
from .util import request


class url():
    def __init__(self, url=None):
        self.url = url

    def req(self, method, **kwargs):
        return request(self.url, method=method, **kwargs)

    def to_s(self):
        return stream(self.url)
