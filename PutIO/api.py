from .models import base


class Files(base):
    def list(self, **kwargs):
        return self.to_u(
            path=[
                'list'
            ],
            query=kwargs
        ).req('get').json()

    def search(self, **kwargs):
        return self.to_u(
            path=[
                'search',
                kwargs.get('query'),
                'page',
                kwargs.get('page_no')
            ],
            query=kwargs
        ).req('get').json()

    def upload(self, **kwargs):
        return self.to_u(
            path=[
                'list'
            ]
        ).req(
            'post',
            data=kwargs
        ).json()

    def create_folder(self, **kwargs):
        return self.to_u(
            path=[
                'create-folder'
            ]
        ).req(
            'post',
            data=kwargs
        ).json()

    def get(self, **kwargs):
        return self.to_u(
            path=[
                kwargs.get('id')
            ],
            query=kwargs
        ).req('get').json()

    def delete(self, **kwargs):
        return self.to_u(
            path=[
                'delete'
            ]
        ).req(
            'post',
            data=kwargs
        ).json()

    def rename(self, **kwargs):
        return self.to_u(
            path=[
                'rename'
            ]
        ).req(
            'post',
            data=kwargs
        ).json()

    def move(self, **kwargs):
        return self.to_u(
            path=['move']
        ).req(
            'post',
            data=kwargs
        ).json()

    def convert_to_mp4(self, **kwargs):
        return self.to_u(
            path=[
                kwargs.get('id'),
                'mp4'
            ]
        ).req(
            'post',
            data=kwargs
        ).json()

    def get_mp4_status(self, **kwargs):
        return self.to_u(
            path=[
                kwargs.get('id'),
                'mp4'
            ]
        ).req('get').json()

    def download(self, id=0):
        return self.to_u(
            path=[
                id,
                'download'
            ]
        ).to_s()

    def zip_and_download(self, **kwargs):
        return self.to_u(
            path=[
                'zip'
            ],
            query=kwargs
        ).to_s()

    def share(self, **kwargs):
        return self.to_u(
            path=[
                'share'
            ],
            query=kwargs
        ).req('post').json()

    def shared(self):
        return self.to_u(
            path=[
                'shared'
            ]
        ).req('get').json()

    def shared_with(self, **kwargs):
        return self.to_u(
            path=[
                kwargs.get('id'),
                'shared-with'
            ]
        ).req('get').json()

    def subtitles(self):
        return self.to_u(
            path=[
                id,
                'subtitles'
            ]
        ).req('get').json()

    def download_subtitle(self, **kwargs):
        return self.to_u(
            path=[
                kwargs.get('id'),
                'subtitles',
                kwargs.get('key')
            ]
        ).req('get').to_s()

    def hls_playlist(self, **kwargs):
        return self.to_u(
            path=[
                kwargs.get('id'),
                'hls',
                'media.m3u8'
            ]
        ).req('get').to_s()

    def events(self):
        return self.to_u(
            path=[
                'events',
                'list'
            ]
        ).req('get').json()

    def events_delete(self):
        return self.to_u(
            path=[
                'events',
                'delete'
            ]
        ).req('post').json()


class Transfers(base):
    def list(self):
        return self.to_u(
            path=[
                'list'
            ]
        ).req('get').json()

    def add(self, **kwargs):
        return self.to_u(
            path=[
                'add'
            ]
        ).req(
            'post',
            data=kwargs
        ).json()

    def get(self, **kwargs):
        return self.to_u(
            path=[
                kwargs.get('id')
            ]
        ).req('get').json()

    def retry(self, **kwargs):
        return self.to_u(
            path=[
                'retry'
            ]
        ).req(
            'post',
            data=kwargs
        )

    def cancel(self, **kwargs):
        return self.to_u(
            path=[
                'cancel'
            ]
        ).req(
            'post',
            data=kwargs
        ).json()

    def clean(self, **kwargs):
        return self.to_u(
            path=[
                'clean'
            ]
        ).req(
            'post',
            data=kwargs
        ).json()


class Friends(base):
    def list(self):
        return self.to_u(
            path=[
                'list'
            ]
        ).req('get').json()

    def friend_requests(self):
        return self.to_u(
            path=[
                'waiting-requests'
            ]
        ).req('get').json()

    def send_request(self, **kwargs):
        return self.to_u(
            path=[
                kwargs.get('username'),
                'request'
            ]
        ).req('post').json()

    def approve(self, **kwargs):
        return self.to_u(
            path=[
                kwargs.get('username'),
                'approve'
            ]
        ).req('post').json()

    def deny(self, **kwargs):
        return self.to_u(
            path=[
                kwargs.get('username'),
                'deny'
            ]
        ).req('post').json()

    def unfriend(self, **kwargs):
        return self.to_u(
            path=[
                kwargs.get('username'),
                'unfriend'
            ]
        ).req('post').json()


class Account(base):
    def info(self):
        return self.to_u(
            path=[
                'info'
            ]
        ).req('get').json()

    def settings(self):
        return self.to_u(
            path=[
                'settings'
            ]
        ).req('get').json()

    def setting_config(self, **kwargs):
        return self.to_u(
            path=[
                'settings'
            ]
        ).req(
            'post',
            data=kwargs
        ).json()
