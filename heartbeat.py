import requests
import warnings
from loguru import logger
import sys

try:
    r = requests.get('http://104.237.234.154:5000/ip', timeout=10)

    if r.status_code == 200:
         logger.add("special.log", filter=lambda record: "special" in record["extra"])
         logger.debug("Client is up")
         logger.bind(special=True).info("Client is up")
    else:
        print("server not found")
except Exception as e:
    logger.debug("Server has been terminated")
    logger.bind(special=True).info("Server has been terminated")