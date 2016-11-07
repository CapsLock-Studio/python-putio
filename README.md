python-putio
===

This is python-styled putio api. Follow this doc: [https://put.io/v2/docs/index.html](https://put.io/v2/docs/index.html)

## Install pip
    sudo easy_install pip

or

    sudo apt-get install python-pip python-dev build-essential



## Install dependencies
    sudo pip install -r requirements.txt


## Example
    import PutIO


    putio = PutIO.oauth_token('{PUT YOUR TOKEN HERE}')
    print putio.Files.list() # as same as (api) /files/list, return json object
    putio.Files.download('12345678').save_to('~/Desktop') # as same as (api) /files/12345678/download, then save it to the Desktop

