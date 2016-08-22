#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import time
import smtplib
from email.mime.text import MIMEText
from urllib.request import urlopen
from bs4 import BeautifulSoup

def sendMail(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'xjr7670@sina.com'
    msg['To'] = 'xjr30226@126.com'

    s = smtplib.SMTP()
    s.connect('smtp.sina.com')
    s.login('xjr7670@sina.com', '')
    s.send_message(msg)
    s.quit()

bsObj = BeautifulSoup(urlopen("https://isitchristmas.com/"), 'lxml')
while (bsObj.find("a", {"id": "answer"}).noscript.get_text() == "不是"):
    print("It is not Christmas yet.")
    time.sleep(3600)
sendMail("It's Christmas!", "According to http://itischristmas.com, it is Christmas!")
