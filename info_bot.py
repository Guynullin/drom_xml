import requests
import time
import logging
from config import BOT_TOKEN, CHAT_ID

def send_message(message:str):
    err = 0
    message = f"<<<DROM to XML>>>\n{message}".replace(BOT_TOKEN, '<token>')
    while True:
        try:
            if err >= 15:
                logging.error('Stopping the send_message function. Exceeded the number of connection attempts')
                break
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
            logging.info(requests.get(url, timeout=60).json())
            break
        except requests.exceptions.ConnectionError as connecterr:
            logging.error(connecterr)
            err += 1
            time.sleep(15)

        except Exception as ex:
            logging.error(ex)
            err += 1
            time.sleep(15)
        
