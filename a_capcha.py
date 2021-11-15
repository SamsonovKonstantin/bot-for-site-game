import webbrowser

from bs4 import BeautifulSoup

import a_boi
import a_login


session=a_login.session

def capcha_find(ather_page,url):
    ssp = BeautifulSoup(ather_page.text,'lxml')
    ssps = ssp.find_all('b')
    for ss in ssps:
        if 'Защита' in ss.text.split(' ')[0]:
            webbrowser.open(url)
            input("Press Enter to continue...")
            
def figth(url):
    page_site = session.get(url)
    soup_page_site = BeautifulSoup(page_site.text, 'lxml')
    if soup_page_site.find('title').text == 'Идёт бой | GWars.Ru':
        return a_boi.fight()
        
def ferm(ather_page):
	ssp = BeautifulSoup(ather_page.text,'lxml')
	ssps = ssp.find_all('td')
	for ss in ssps:
	           if 'Ворота' in ss.text.split(' ')[0]:
	           	webbrowser.open('https://www.gwars.ru/ferma.php?')
	           	input("Press Enter to continue...")
	           	