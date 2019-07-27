from pyLatch.latchreq import LatchReq
from pyLatch.latchapp import LatchApp

STATUS_API = 'status/'
PAIR_API = 'pair/'
UNPAIR_API = 'unpair/'

class Latch(LatchApp):
  def __init__(self, appid, secret):
    """
    Class constructor
    :param appid: App ID
    :param secret: Secret code
    """
    super().__init__(appid, secret)

  def pair(self, paircode):
    """
    Returns JSON pair data
    :param paircode: Pair Code
    :return: JSON pair data
    """
    return LatchReq(self._appid, self._secret).http(PAIR_API + paircode, PAIR_API + paircode)

  def status(self, accountID):
    """
    Returns JSON status data
    :param accountID: Account ID
    :return: JSON status data
    """
    return LatchReq(self._appid, self._secret).http(STATUS_API + accountID, STATUS_API + accountID)

  def unpair(self, accountID):
    """
    Returns JSON unpair
    :param accountID: Account ID
    :return: JSON unpair data
    """
    return LatchReq(self._appid, self._secret).http(UNPAIR_API + accountID, UNPAIR_API + accountID)
