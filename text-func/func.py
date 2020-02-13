import io
import json
import requests
import fdk
from fdk import response

def apicall():
    url = "https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json"

    payload = {'Body': 'Hello there, from OCI.',
    'To': '+12345',
    'From': '+12345'}
    files = [

    ]
    headers = {
     'account_sid': 'LK88ea8d8a087c7ad',
      'Authorization': 'Basic 87vzlhuadfyklh8wODQ4OTkzOGY2Yzo1Zjg1ZWM5OW08754671487149876142NA=='
    }

    response = requests.request("POST", url, headers=headers, data = payload, files = files)

    print(response.text.encode('utf8'))

apicall()