import requests
import time
import datetime
from hashlib import sha1
import hmac
import binascii

ELEVEN_URL = 'https://latch.elevenpaths.com'
API_VERSION = '1.3'
API_BODY = '/api/'
STATUS_API = 'status/'
PAIR_API = 'pair/'
UNPAIR_API = 'unpair/'

class Latch():
  def __init__(self, appid, secret):
    self._appid = appid
    self._secret = secret
    self._proxy = None

  @property
  def appid(self):
    '''Returns AppID'''
    return self._appid

  @property
  def secret(self):
    '''Returns secret'''
    return self._secret

  @property
  def proxy(self):
    '''Returns the used proxy'''
    return self._proxy

  def setProxy(self, host, port):
    '''Enable use of proxy'''
    self._proxy = {
      'http': '{}:{}'.format(host, port), 
      'https': '{}:{}'.format(host, port)
    }

  def _http(self, signature, api):
    '''HTTP request method'''
    date = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    headers = {
      'Authorization': '11PATHS {} {}'.format(self._appid, self.signature(date, signature)),
      'X-11Paths-Date': date
    }

    with requests.Session() as s:
      if self._proxy != None:
        s.proxies = self._proxy
      s.headers = headers

      resp = s.get('{}{}{}/{}'.format(ELEVEN_URL, API_BODY, API_VERSION, api))

    return resp.json()
  
  def signature(self, datetime, token):
    '''Returns authorization hash'''
    sig_str = 'GET\n{}\n\n{}{}/{}'.format(datetime, API_BODY, API_VERSION, token)
    sha1_hash = hmac.new(self._secret.encode(), sig_str.encode(), sha1)
    return binascii.b2a_base64(sha1_hash.digest())[:-1].decode('utf8')

  def pair(self, paircode):
    return self._http(PAIR_API + paircode, PAIR_API + paircode)

  def status(self, accountID):
    return self._http(STATUS_API + accountID, STATUS_API + accountID)

  def unpair(self, accountID):
    return self._http(UNPAIR_API + accountID, UNPAIR_API + accountID)