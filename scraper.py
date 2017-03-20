import requests
from AESCipher import AESCipher

cid = '96f2ea05-8742-401d-aa42-ec269f8a71c0'
link = 'https://apitest.sewadwaar.rajasthan.gov.in/app/live/webServicesRepository/getFetchDetailsEncryptedBySso/WithEncryption?client_id='+cid
print(link)

data = {'SRVID':'1214','searchKey':'9352423664','SSOID':'SSOTESTKIOSK'}
def encrypt(data):
    key = 'E-m!tr@2016'
    cipher = AESCipher(key)
    enc = cipher.encrypt(str(data))
    return enc

enc_data = encrypt(data)
enc_data = r'05jMkbnJAHEBPte1IWEhFxa8ODS01Axt7OQmAClhvthWKULyJWHRNY6X7/bqD53regvYLnGTf9AXc0qIvU9FBMPnlMViuAy7pth5bXa5jfs='
data={'encData':enc_data}
r = requests.post(link, data=data)
print(r)
print(r.text)
