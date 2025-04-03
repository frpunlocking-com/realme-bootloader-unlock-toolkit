import os
import base64
import requests
import json
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography import x509

#HOST       = 'lk.realmemobile.com' # Chinese servers (they are unlock different models)
HOST       = 'lkf.realmemobile.com' # Not-Chinese servers

# MODEL      = 'RMX3709EX'
# OTAVERSION = 'RMX3700_11.G.88_8888_202305070042'
# ROMVERSION = 'RMX3700_13.1.0.506(EX01)'

MODEL      = 'RMX3660'                           # INSERT your model data
OTAVERSION = 'RMX3660_11.A.44_0440_202309231931' # INSERT your model data
ROMVERSION = 'RMX3660_11_A.44'          # INSERT your model data

# MODEL      = 'RMX3701'
# OTAVERSION = 'RMX3701_11.C.21_1210_202401191916'
# ROMVERSION = 'RMX3701_14.0.0.210(EX01)'

SERIAL     =  '0x1b99999'
IMEI1      =  '867215099999999'
TOKEN      =  'TOKEN_***'
LANGUAGE   = 'en-GB'

# from GT5-DeepTesting/assets/lk_unlock.crt
PEM_DATA = b'''-----BEGIN CERTIFICATE-----
MIIDZzCCAk+gAwIBAgIEbHDjwzANBgkqhkiG9w0BAQsFADBkMQswCQYDVQQGEwJD
TjESMBAGA1UECBMJR3VhbmdEb25nMQ0wCwYDVQQHEwRTSFpIMQ0wCwYDVQQKEwRP
UFBPMQ0wCwYDVQQLEwRPUFBPMRQwEgYDVQQDEwtjb2xvcm9zLmNvbTAeFw0yMDAz
MTkwNDM1MzhaFw0yMDA2MTcwNDM1MzhaMGQxCzAJBgNVBAYTAkNOMRIwEAYDVQQI
EwlHdWFuZ0RvbmcxDTALBgNVBAcTBFNIWkgxDTALBgNVBAoTBE9QUE8xDTALBgNV
BAsTBE9QUE8xFDASBgNVBAMTC2NvbG9yb3MuY29tMIIBIjANBgkqhkiG9w0BAQEF
AAOCAQ8AMIIBCgKCAQEAuMQtp8+d4x3XtX03uxos/bFm7tisY1h9Wq5Dayq8q0XA
dvIgvHsLxQCsjWtL9OgRZlrBxVLllYRvevNdp3Lc9AznjRm7Iz/6pcgYVQCI2Raf
RBHlWSMYD3jheKcOv27XwvnBkRGPOEUcoA0VS/cQYCiFL4NuRGlvVGI2o0/mgVe2
lpt8UDbgarz61k+b7FyfrKYMBPxZiFvs1csGCgz5HZQicOFdyYQNdPGWLBnHyZ/J
QFwnfWkkSj6d+24e5Ow5Wf0MCectNL0UN8rZGLZeffCXsbua52d3cnFjqpTBMFjo
Se/VzfJHsFYTsyd2acI7URGKeYEE6iSn7plGVNVnJwIDAQABoyEwHzAdBgNVHQ4E
FgQUhF6wKou65vkgLTCFC26WXNHTGuQwDQYJKoZIhvcNAQELBQADggEBAFx+aoVJ
TmvKj0brs+ips3RP8Ih9/OqmHd64AF1FgIovoSnMFUlU77bq41UL0j3H6szGMY/q
bKJ/L2N4ovtFXT/zGj/TTDKpzpqdrlDwVWR7rilgOQF5ZDZjUEBMrGQnIDuAPciX
H5taP+AltFtQ+aTMsHWPNhF8dEO9PoAiDbjOQ1/ORSEqKFmZ8p+5zt352BuLFJrQ
AuEBXf88KSmsXoqe+Jmnhw8GKl5CwPL62ZiGNmxCLHbmQ7JXNSRgbTxEFRcP50jY
L560vBj3/Q9gIwo2nQXQmx7QJRXkRmAzauF1GQO66xLewcsIUAziOmPKoOI0NxiK
UIRhPQkaVOk9BcA=
-----END CERTIFICATE-----'''

def PrepareHeaders(key):
    pub_key = x509.load_pem_x509_certificate(PEM_DATA).public_key()
    enc_key = pub_key.encrypt(base64.b64encode(key), padding.PKCS1v15())

    return {
        'model': MODEL,
        'otaVersion': OTAVERSION,
        'language': LANGUAGE,
        'key': base64.b64encode(enc_key).decode(),
        'romVersion': ROMVERSION,
        'colorOSVersion': '',
        'androidVersion': '13',
        'trackRegion': '',
        'uRegion': '',
        'Content-Type': 'application/json; charset=utf-8',
        'Host': HOST,
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.12.2'
        }

def PrepareParams(key):
    sent_data = {
        'clientLockStatus': 0,
        'udid': IMEI1,
        'model': MODEL,
        'operator': '',
        'otaVersion': OTAVERSION,
        'chipId': SERIAL,
        'token': TOKEN
        }
    enc_data = json.dumps(sent_data, separators=(',', ':'), ensure_ascii=False)

    digest = hashes.Hash(hashes.MD5())
    digest.update(key)
    md5_raw = digest.finalize()

    encryptor = Cipher(algorithms.AES(key), modes.CTR(md5_raw)).encryptor()
    enc = encryptor.update(enc_data.encode()) + encryptor.finalize()
    return json.dumps({'params': base64.b64encode(enc).decode()}, separators=(',', ':'), ensure_ascii=False)

def Decrypt(key, data):
    digest = hashes.Hash(hashes.MD5())
    digest.update(key)
    md5_raw = digest.finalize()

    decryptor = Cipher(algorithms.AES(key), modes.CTR(md5_raw)).decryptor()
    dec = decryptor.update(data) + decryptor.finalize()
    return dec.decode()

key_raw = os.urandom(32)

print('Used key: ' + base64.b64encode(key_raw).decode())
hdrs = PrepareHeaders(key_raw)
print('Sent headers: ', hdrs)
params = PrepareParams(key_raw)
print('Sent body: ', params)

# this request just always launched in DeepTesting, unknown purpose
#response = requests.post(f'https://{HOST}/api/v2/get-all-status', data = params, headers = hdrs)
# this request checks unlock application status
response = requests.post(f'https://{HOST}/api/v2/check-approve-result', data = params, headers = hdrs)
# this request starts unlock application
#response = requests.post(f'https://{HOST}/api/v2/apply-unlock', data = params, headers = hdrs)
# also in DeepTesting code they have /lock-client, /update-client-lock-status
print('Response code:', response.status_code)
print('Response headers:', response.headers)
print('Response data:', response.text)

resp = json.loads(response.text)
data = base64.b64decode(resp['resps'])

dec = Decrypt(key_raw, data)
print('Decoded response:', dec)