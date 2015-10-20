from .api import Files, Transfers, Friends, Account


class oauth_token():
    def __init__(self, oauth_token=None):
        self.oauth_token = oauth_token
        self.Files = Files(oauth_token)
        self.Transfers = Transfers(oauth_token)
        self.Friends = Friends(oauth_token)
        self.Account = Account(oauth_token)
