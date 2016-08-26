#!/usr/bin/env python3

import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('ryan', 'password')
r = requests.post(url="http://www.pythonscraping.com/pages/auth/login.php", auth=auth)
print(r.text)
