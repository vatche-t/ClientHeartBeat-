import pickle 
import os
from datetime import datetime
import requests




def send_to_telegram(message):

    apiToken = '5977566963:AAEVWXcwN9miRHLyq2etTq-qP1w8wFsrz90'
    chatID = '260376634'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)


def get_ips():
    results = []
    testdir = "../../last_beat"
    for f in os.listdir(testdir):
        if f.endswith(''):
            results.append(f)
    return results



def check_client():

    #for filename in [f'../last_beat/{ip}' for ip in get_ips()]:
    for ip in get_ips():
        filename = f'../../last_beat/{ip}'
        with open(filename, 'rb')as file:
            fc = file.read()
            time_stamp = pickle.loads(fc)
            #return time_stamp
        now = datetime.utcnow()
        if (now - time_stamp).total_seconds() > 60 * 200:
            send_to_telegram(f"Client {ip} has been disconnected for more than 20 minutes at: {time_stamp}")
        else:
               send_to_telegram(f"client {ip} is connected....")

check_client()      

