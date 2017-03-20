import requests

cid = '96f2ea05-8742-401d-aa42-ec269f8a71c0'
link = 'https://apitest.sewadwaar.rajasthan.gov.in/app/live/webServicesRepository/getFetchDetailsEncryptedBySso/WithEncryption?client_id='+cid
print(link)

data = {'SRVID':'1214','searchKey':'9352423664','SSOID':'SSOTESTKIOSK'}
def encrypt(data):
    return data

enc_data = encrypt(data)
data={'encData':enc_data}
r = requests.post(link, data=data)
print(r)
print(r.text)
