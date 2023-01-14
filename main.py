import subprocess
import time


while True: 
    process = subprocess.run(['python3', 'client.py'], timeout=40)
    time.sleep(5)

