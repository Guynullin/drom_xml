import requests
import logging
import copy
from bs4 import BeautifulSoup
from config import URL, LOGFILE, WEB_PATH
from info_bot import send_message
from compare import compare

def main():
    logging.basicConfig(level=logging.INFO, filename=LOGFILE, filemode='a',\
                    format="%(asctime)s %(levelname)s %(message)s")
    try:

        err = 0
        logging.info('\n\nStart')

        while True:

            if err >= 15:
                logging.error('Exceeded the number of connection attempts')
                send_message('Error\nExceeded the number of connection attempts')
                break
        
            resp = requests.get(url=URL)

            if resp.status_code == 200:

                soup = BeautifulSoup(resp.content, 'lxml').find('yml_catalog')

                soup_origin = BeautifulSoup(resp.content, 'lxml').find('yml_catalog')
                
                for price in soup.select('price'):
                    price.string = f"{float(price.string) * 4:.{2}f}" 

                if compare(soup.prettify(), soup_origin.prettify()) == 1:
                    with open(WEB_PATH, 'w') as file:
                        file.write(soup.prettify())
                    logging.info('Success')
                    send_message('Success')
                    break
                else:
                    logging.error('compare return 0')
                    break
            
    except Exception as ex:
        logging.error(ex)
        send_message(f'Error\n{ex}')


if __name__ == '__main__':
    main()




