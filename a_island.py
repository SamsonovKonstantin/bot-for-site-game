import requests
import lxml
import time

from bs4 import BeautifulSoup

import a_login
import a_capcha
import a_fight
import a_vooruj

session = a_login.session

def info_island():
    url='https://www.gwars.ru/walk.p.php?welcome'
    page_island = session.get(url)
    soup_page_island = BeautifulSoup(page_island.text, 'lxml')
    hash_map=soup_page_island.find('a',{'id':'a_2_m6'})['href'].split('=')[-1]
    print(hash_map)
    a_capcha.capcha_find(page_island,url)
    return soup_page_island
    
def fight_island():
    url='https://www.gwars.ru/walk.p.php?welcome'
    page_island = session.get(url)
    soup_page_island = BeautifulSoup(page_island.text, 'lxml')
    try:
        if soup_page_island.find('span',class_='redlightfont').text == "Выход в прибрежную зону возможен после 80% HP":
            pass
    except:
        fpi=soup_page_island.find_all('a')
        for red1 in fpi:
            if red1['href'].split('&')[-1] == 'red=1':
                next_step=session.get('https://www.gwars.ru'+red1['href'])
                time.sleep(30)
                a_capcha.figth('https://www.gwars.ru'+red1['href'])
                break
        print('Нет ботов для драки')
    		
fight_island()
p_vooruj.workshop()
p_vooruj.putset()

    		
'''
    url1=f'https://www.gwars.ru/walk.p.php?w=2&wx=8&wy=4&xc={hhhs}'
    ppp = session.get(url1)
    p_capcha.capcha_find(ppp,url1)
    
    url2=f'https://www.gwars.ru/walk.p.php?w=2&wx=-8&wy=-4&xc={hhhs}'
    mmm=session.get(url2)
    p_capcha.capcha_find(mmm,url2)
'''
