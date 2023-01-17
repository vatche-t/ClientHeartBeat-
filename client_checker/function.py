import pickle 
import os
from datetime import datetime

# import smtplib
# import ssl
# from email.message import EmailMessage

# email_sender = 'vatche.selleryar@gmail.com'
# email_password = 'xvoiaghwmzdmpwdu'
# email_receiver = 'vatche.thorossian@gmail.com'


# subject = 'Client has been disconnected for to long!!'
# body = """
# Your client has been disconnected for more than 20 minutes.
# """

# em = EmailMessage()
# em['From'] = email_sender
# em['To'] = email_receiver
# em['Subject'] = subject
# em.set_content(body)

# context = ssl.create_default_context()

def get_ips():
    results = []
    testdir = "../last_beat"
    for f in os.listdir(testdir):
        if f.endswith(''):
            results.append(f)
    return results



def check_client():
    #for filename in [f'../last_beat/{ip}' for ip in get_ips()]:
    for ip in get_ips():
        filename = f'../last_beat/{ip}'
        with open(filename, 'rb')as file:
            fc = file.read()
            time_stamp = pickle.loads(fc)
            #return time_stamp
        now = datetime.utcnow()
        if (now - time_stamp).total_seconds() > 60 * 200:
            print(f'Client {ip} has been disconnected for more than 20 minutes at: {time_stamp}')
            return ip
        else:
               print(f"client {ip} is connected....")

check_client()      

# present = datetime.now()


# diff = (present - time_stamp() ).total_seconds() 

# if diff > 20 :
#     with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
#         smtp.login(email_sender, email_password)
#         smtp.sendmail(email_sender, email_receiver, em.as_string())
# else:
#     print("client is connected....")
