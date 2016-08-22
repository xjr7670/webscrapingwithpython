#!/usr/bin/env python3

import smtplib
from email.mime.text import MIMEText

msg = MIMEText("The body of the email is here")

msg['Subject'] = "An Email Alert"
msg['From'] = 'xjr7670@sina.com'
msg['To'] = 'xjr30226@126.com'

s = smtplib.SMTP('smtp.sina.com')
s.login('xjr7670@sina.com', '')
s.send_message(msg)
s.quit()
