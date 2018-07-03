import base64
import hashlib
import requests
from datetime import datetime


    headers = {"Authorization": "Bearer %s" % access_token}
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        request = {
            "BusinessShortCode": self.shortcode,
            "Password": self._generate_password(timestamp),
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": str(int(amount)),
            "PartyA": phone_number,
            "PartyB": str(self.shortcode),
            "PhoneNumber": phone_number,
            "CallBackURL": callback_url,
            "AccountReference": reference,
            "TransactionDesc": description
        }
        url = self.server + self.process_request_path
        response = requests.post(url, json=request, headers=headers)
        data = response.json()