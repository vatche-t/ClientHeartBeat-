import pickle 
import os
from datetime import datetime

import smtplib
import ssl
from email.message import EmailMessage

email_sender = '[sender email]'
email_password = '[sender pass]'
email_receiver = '[receiver email]'


def get_ips():
    results = []
    testdir = "../../last_beat"
    for f in os.listdir(testdir):
        if f.endswith(''):
            results.append(f)
    return results



def check_client():


    context = ssl.create_default_context()
    #for filename in [f'../last_beat/{ip}' for ip in get_ips()]:
    for ip in get_ips():
        filename = f'../../last_beat/{ip}'
        with open(filename, 'rb')as file:
            fc = file.read()
            time_stamp = pickle.loads(fc)
            #return time_stamp
        now = datetime.utcnow()
        if (now - time_stamp).total_seconds() > 60 * 200:
             with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                                    
                subject = 'Client has been disconnected for to long!!'
                body = f"""
                'Client {ip} has been disconnected for more than 20 minutes at: {time_stamp}'
                """
                em = EmailMessage()
                em['From'] = email_sender
                em['To'] = email_receiver
                em['Subject'] = subject
                em.set_content(body)
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())
        else:
               print(f"client {ip} is connected....")

check_client()      

