#!/usr/bin/env python3

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 
# create message object instance
message = MIMEMultipart()

import getpass

username = input('Enter your username:')
password = getpass.getpass(prompt='Enter your password:')

# setup the parameters of the message
message['From'] = username
message['To'] = username
message['Subject'] = "Subject"
 
# add in the message body
message.attach(MIMEText("message", 'plain'))
 
#create server
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()
 
# Login Credentials for sending the mail
server.login(message['From'], password)
 
 # send the message via the server.
server.sendmail(message['From'], message['To'], message.as_string())
print("successfully sent email to %s:" % (message['To']))
server.quit()