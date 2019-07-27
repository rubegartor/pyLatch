# PyLatch
![https://img.shields.io/badge/Python-3.6%20%7C%203.7-blue.svg](https://img.shields.io/badge/Python-3.6%20%7C%203.7-blue.svg) ![https://img.shields.io/badge/version-1.1.0-orange.svg](https://img.shields.io/badge/version-v1.1.0-orange.svg) ![https://img.shields.io/badge/API%20Version-v1.3-brightgreen.svg](https://img.shields.io/badge/API%20Version-v1.3-brightgreen.svg)

A simple and basic API wrapper for Latch written in Python

## Installation
```bash
# Windows
python -m pip install pyLatch
#Linux/OS X
python3 -m pip install pyLatch
```
## Code Examples
**Basic code:**
```python
import pyLatch
pyLatch.Latch('APPID', 'APPSECRET')
```
**How to pair:**
```python
import pyLatch
latch = pyLatch.Latch('APPID', 'APPSECRET')
resp = latch.pair('pairCode')
# resp = {'data': {'accountId': 'accountID'}}
```
**Obtaining status:**
```python
import pyLatch
latch = pyLatch.Latch('APPID', 'APPSECRET')
resp = latch.status('accountID')
# resp = {'data': {'operations': {'APP_ID': {'status': 'on'}}}}
```
**Unpair account:**
```python
import pyLatch
latch = pyLatch.Latch('APPID', 'APPSECRET')
resp = latch.unpair('accountID')
# resp = {}
```
**Use custom proxy:**
```python
import pyLatch
latch = pyLatch.Latch('APPID', 'APPSECRET')
latch.setProxy('PROXY_HOST', 'PROXY_PORT')
```