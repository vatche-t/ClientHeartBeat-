import pandas as pd
import re



def file_reader():
    file = r"app/client.log"

    logs = []
    phrase = ["INFO:werkzeug:"]

    with open(file) as f:
        f = f.readlines()

    for line in f:
        for phrase in phrase:
            if phrase in line:
                logs.append(line)
                break

    return(logs)
def status_code_latest():
    latest = file_reader()[-1]
    number = re.findall(r'\d+',latest)
    return number[-1]
def status_code_second_latest():
    latest = file_reader()[-1]
    number = re.findall(r'\d+',latest)
    number[-2]

if status_code_latest() == '200':
    print("client is  connected")
else:
    print("status: server error")