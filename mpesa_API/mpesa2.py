import base64
import requests
import hashlib
from datetime import datetime
import base64
import json


access_token_path = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials' 
consumer_key="ELaBRaUrjYBJPeN8ImXC5rb7yQCxmsJA"
consumer_password="4AhsWhDLYHxJyAuP"
response = requests.get(access_token_path, auth=(consumer_key, consumer_password)).text
res=json.loads(response)
access_token =res ['access_token']
timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
passphrase="bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
phoneNumber=int(input("enter number "))
BusinessShortCode=174379
pasword=requests.get(base64.b64encode(BusinessShortCode + timestamp + passphrase)).text
pas=json.loads(password)
Passwords=pas['password']

api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
headers = { "Authorization": "Bearer %s" % access_token  }
request = {
  "BusinessShortCode": "174379 ",
  "Password": passwords,
  "Timestamp": timestamp,
  "TransactionType": "CustomerPayBillOnline",
  "Amount": "1",
  "PartyA":phoneNumber,
  "PartyB": " 174379",
  "PhoneNumber": phoneNumber,
  "CallBackURL": "http://requestbin.fullcontact.com/18ggrma1",
  "AccountReference": "test",
  "TransactionDesc": "test"
}
def get_access_token():
        url = api_url + access_token_path
        response = requests.get(url, auth=(consumer_key, consumer_password))
        if response.status_code == 200:
            data = response.json()
            access_token = data['access_token']
            return access_token
        else:
            return None
def _generate_password():
    password = BusinessShortCode + timestamp + passphrase
    return base64.b64encode(password)
    password= _generate_password()

def transaction_status_request(phone_number):
 timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
 access_token = get_access_token()

response = requests.post(api_url, json = request, headers=headers)
print(response.text)
