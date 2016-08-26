#!/usr/bin/env python3

import requests

session = requests.Session()

params = {'username': 'username', 'password': 'password'}
s = session.post("http://www.pythonscraping.com/pages/cookies/welcome.php", params)
print("Cookie is set to: ")
print(s.cookies.get_dict())
print("------------------")
print("Going to profile page...")
s = session.get("http://www.pythonscraping.com/pages/cookies/profile.php")
print(s.text)
