import logging
from bs4 import BeautifulSoup
from info_bot import send_message

def compare(drom_mod: str, drom_orig:str):

    soup1 = BeautifulSoup(drom_mod, 'lxml')

    soup2 = BeautifulSoup(drom_orig, 'lxml')

    offers1 = soup1.find_all('offer')
    offers2 = soup2.find_all('offer')
    count = 0
    
    for offer1 in offers1:
        price1 = offer1.find('price').text
        offer1price = float(price1)
        for offer2 in offers2:
            if offer1.get('id') == offer2.get('id'):
                offer2price = float(offer2.find('price').text)
                if offer1price != offer2price * 4:
                    logging.error(f"{offer1.get('id')} : {offer1price} != {offer2.get('id')} : {offer2price}")
                    count += 1
                break

    if count != 0:
        send_message('Error\nOffers not equals!')
        return 0
    else:
        return 1