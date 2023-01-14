import pickle 
import os
from datetime import datetime, timedelta
import datetime as dt




import smtplib
import ssl
from email.message import EmailMessage

email_sender = '[your email address]'
email_password = '[your password]'
email_receiver = '[recipient email]'


subject = 'Client has been disconnected for to long!!'
body = """
Your client has been disconnected for more than 20 minutes.
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

def time_stamp():
    with open('..//127.0.0.1.last', 'rb')as file:
        fc = file.read()
        time_stamp = pickle.loads(fc)
        return time_stamp

present = datetime.now()


diff = (present - time_stamp() ).total_seconds() 

if diff > 1200 :
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
else:
    print("client is connected....")
