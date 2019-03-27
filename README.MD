# PyLatch
![https://img.shields.io/badge/Python-3.6%20%7C%203.7-blue.svg](https://img.shields.io/badge/Python-3.6%20%7C%203.7-blue.svg) ![https://img.shields.io/badge/version-1.0.0-orange.svg](https://img.shields.io/badge/version-v1.0.0-orange.svg) ![https://img.shields.io/badge/API%20Version-v1.3-brightgreen.svg](https://img.shields.io/badge/API%20Version-v1.3-brightgreen.svg)

A simple and basic API wrapper for Latch written in Python
## Code Examples
**Basic code:**
```python
from pyLatch import pyLatch
pyLatch.Latch('APPID', 'APPSECRET')
```
**How to pair:**
```python
from pyLatch import pyLatch
latch = pyLatch.Latch('APPID', 'APPSECRET')
resp = latch.pair('pairCode')
# resp = {'data': {'accountId': 'accountID'}}
```
**Obtaining status:**
```python
from pyLatch import pyLatch
latch = pyLatch.Latch('APPID', 'APPSECRET')
resp = latch.status('accountID')
# resp = {'data': {'operations': {'APP_ID': {'status': 'on'}}}}
```
**Unpair account:**
```python
from pyLatch import pyLatch
latch = pyLatch.Latch('APPID', 'APPSECRET')
resp = latch.unpair('accountID')
# resp = {}
```
**Use custom proxy:**
```python
from pyLatch import pyLatch
latch = pyLatch.Latch('APPID', 'APPSECRET')
latch.setProxy('PROXY_HOST', 'PROXY_PORT')
```