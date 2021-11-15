import requests
import lxml
import webbrowser

from bs4 import BeautifulSoup

import a_login
import main


sets=main.sets
session = a_login.session
URL='https://www.gwars.ru'

def workshop():
    i=0
    while i<5:
        ws_page = session.get(URL + '/workshop.php?')
        soup_ws_page = BeautifulSoup(ws_page.text,'lxml')
        rems = soup_ws_page.find_all('a')
        for rem in rems:
            if rem.text == 'Ремонтировать':
                session.get(URL+rem['href'])
        i=i+1
    return ('Ремонт окончен')

def putset():
    ps_page=session.get(URL+'/items.php')
    soup_ps_page=BeautifulSoup(ps_page.text,'lxml')
    nobrs=soup_ps_page.find_all('nobr')
    for nobr in nobrs:
        try:
            if nobr.find('b').text == f'{sets}.':
                if nobr.find('a'):
                    session.get(URL+nobr.find('a')['href'])
                    print(f'Надел комплект №{sets}')
                else:
                    print('Не хватает вещей для комплекта')
                    webbrowser.open(URL+'/items.php')
                    input("Press Enter to continue...")
        except:
            pass

#workshop()
#putset()