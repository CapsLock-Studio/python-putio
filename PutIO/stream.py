import re
from .util import request


class stream():
    def __init__(self, url=None):
        self.url = url

    def save_to(self, save_path=None):
        data = request(self.url, 'get', stream=True)
        with open(
            '%s/%s' % (
                save_path,
                re.findall(
                    'filename=["]*([^"]+)["]*',
                    data.headers.get('content-disposition')
                ).pop()
            ),
            'wb'
        ) as fn:
            map(
                lambda x: fn.write(x),
                data
                .iter_content(chunk_size=1024)
            )
            fn.close()
