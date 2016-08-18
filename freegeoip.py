#!/usr/bin/env python3

import json
from urllib.request import urlopen

def getCountry(ipAddress):
    response = urlopen("http://freegeoip.net/json/" + ipAddress).read().decode("utf-8")
    responseJson = json.loads(response)
    return responseJson

ipinfo = getCountry("104.194.88.19")
print("IP Address: ", ipinfo["ip"])
print("Country_Code: ", ipinfo["country_code"])
print("Country_Name: ", ipinfo["country_name"])
print("Region_code: ", ipinfo["region_code"])
print("Region_Name: ", ipinfo["region_name"])
print("City: ", ipinfo["city"])
print("Zip_Code: ", ipinfo["zip_code"])
print("Latitude", ipinfo["latitude"])
print("Longitude", ipinfo["longitude"])
