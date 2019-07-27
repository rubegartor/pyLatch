from pyLatch.latchapp import LatchApp
from datetime import datetime
from hashlib import sha1
import requests
import binascii
import hmac
import time

URL = 'https://latch.elevenpaths.com'
API_VERSION = '1.3'
API_BODY = '/api/'

class LatchReq(LatchApp):
  def __init__(self, appid, secret):
    super().__init__(appid, secret)

  def http(self, signature, api):
    """
    HTTP request method
    :param signature: Siganture
    :param api: API
    :return: JSON response data
    """
    date: str = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    headers = {
      'Authorization': '11PATHS {} {}'.format(self._appid, self.__signature(date, signature)),
      'X-11Paths-Date': date
    }

    with requests.Session() as s:
      if self._proxy is not None:
        s.proxies = self._proxy
      s.headers = headers

      resp = s.get('{}{}{}/{}'.format(URL, API_BODY, API_VERSION, api))

    return resp.json()

    
  def __signature(self, dt, token):
    """
    Returns authorization hash
    :param dt: Formated DateTime (%Y-%m-%d %H:%M:%S)
    :param token: Token
    :return: Signature of authorization header
    """
    sig_str = 'GET\n{}\n\n{}{}/{}'.format(dt, API_BODY, API_VERSION, token)
    sha1_hash = hmac.new(self._secret.encode(), sig_str.encode(), sha1)
    return binascii.b2a_base64(sha1_hash.digest())[:-1].decode('utf8')
