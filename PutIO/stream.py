from .util import request


class stream():
    def __init__(self, url=None):
        self.url = url

    def save_to(self, save_path=None):
        with open(save_path, 'wb') as fn:
            map(
                lambda x: fn.write(x),
                request(self.url, 'get', stream=True)
                .iter_content(chunk_size=1024)
            )
            fn.close()
