class LatchApp(object):
  def __init__(self, appid, secret):
    """
    Class constructor
    :param appid: App ID
    :param secret: Secret code
    """
    self._appid = appid
    self._secret = secret
    self._proxy = None

  @property
  def appid(self):
    """
    Returns App ID
    :return: App ID
    """
    return self._appid

  @property
  def secret(self):
    """
    Returns Secret
    :return: Secret
    """
    return self._secret

  @property
  def proxy(self):
    """
    Returns Proxy
    :return: Proxy
    """
    return self._proxy

  def setProxy(self, host, port):
    """
    Set proxy data
    :param host: Proxy Host
    :param port: Proxy Port
    """
    self._proxy = {
      'http': '{}:{}'.format(host, port), 
      'https': '{}:{}'.format(host, port)
    }
