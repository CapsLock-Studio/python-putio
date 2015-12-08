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


## Copyright / License

Copyright 2015 CapsLock, Studio.

Licensed under the GNU General Public License Version 2.0 (or later); you may not use this work except in compliance with the License.

You may obtain a copy of the License in the LICENSE file, or at: [http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt](http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt)

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

See the License for the specific language governing permissions and limitations under the License.
