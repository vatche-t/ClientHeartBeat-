import subprocess
import time


while True: 
    process = subprocess.run(['python3', 'function.py'], timeout=40)
    time.sleep(5)

