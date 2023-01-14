import pickle 
import os
from datetime import datetime, timedelta
import datetime as dt



def time_stamp():
    with open('..//127.0.0.1.last', 'rb')as file:
        fc = file.read()
        time_stamp = pickle.loads(fc)
        return time_stamp

present = datetime.now()


diff = (present - time_stamp() ).total_seconds() 

if diff > 10 :
    print('The client has been disconnected for more than 10  seconds.')
else:
    print("client is connected....")