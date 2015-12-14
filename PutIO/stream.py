import re
import grequests
from .util import request


class stream():
    def __init__(self, url=None):
        self.url = url

    def fork(self, fork):
        self.fork = fork
        return self

    def save_to(self, save_path=None):
        try:
            data = request(self.url, 'get', stream=True)
            data_headers = data.headers
            title = re.findall(
                'filename=["]*(.+)["]*',
                data_headers.get('content-disposition')
            ).pop()
            length = int(data_headers.get('content-length'))
            try:
                self.fork = self.fork
            except Exception:
                self.fork = 1
            slice_length = int((int(length) / self.fork))
            headers = []
            start = 0
            while start <= length:
                end = start + slice_length
                if end >= length:
                    end = length
                headers.append([
                    'Content-Length: %s' % (end - start),
                    'Range: bytes=%s-%s/%s' % (start, end, length)
                ])
                start = start + slice_length + 1
            rs = [grequests.get(self.url, headers=h, stream=True) for h in headers]
            print rs
            req = grequests.map(rs)
            print req
            # for val in grequests.map(rs):
                # map(lambda x: fn.write(x), val.iter_content(chunk_size=1024))
            # fn.close()
        except Exception as e:
            print e
            self.save_to(save_path=save_path)
