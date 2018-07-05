import requests

access_token = "Access-Token"
api_url = "https://sandbox.safaricom.co.ke/mpesa/b2b/v1/paymentrequest"
headers = { "Authorization": "Bearer %s" % access_token }
request = {
  "Initiator": " ",
  "SecurityCredential": " ",
  "CommandID": " ",
  "SenderIdentifierType": " ",
  "RecieverIdentifierType": " ",
  "Amount": " ",
  "PartyA": " ",
  "PartyB": " ",
  "AccountReference": " ",
  "Remarks": " ",
  "QueueTimeOutURL": "http://your_timeout_url",
  "ResultURL": "http://your_result_url"
}

response = requests.post(api_url, json = request, headers=headers)

print (response.text)
