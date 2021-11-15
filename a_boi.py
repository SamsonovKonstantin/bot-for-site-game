import time
import random
from bs4 import BeautifulSoup

import a_login


url=a_login.url
session=a_login.session
url_boi='/wargroup.php?war=armed'
url_zayavka='&form=1'

def zayavka_group():
	a=session.get(url+url_boi+url_zayavka)
	sa=BeautifulSoup(a.text,'lxml')
	s=sa.find('form').find('input', {'name':'lopata'})['value']
	print(s)

def zayavka_solo():
	a=session.get('https://www.gwars.ru/warlist.php?war=armed')
	sa=BeautifulSoup(a.text,'lxml')
	a_login.ppp(a,sa)
	b=sa.find('a',{'class':'mainbutton'})['href']
	print(url+b)

def fight():
    url_f = 'https://www.gwars.ru/map.php'
    f_page=session.get(url_f)
    s_f_page = BeautifulSoup(f_page.text,'lxml')
    if s_f_page.find('title').text == 'Идёт бой | GWars.Ru':
        try:
            if s_f_page.find('div', id="cntdown").text.split(' ')[0] == 'Страница':
                time.sleep(3)
                return fight()
        except:
            f_form = s_f_page.find('form', id='battleform')

            turn = f_form.find('input', {'name':'turn'})['value']
            bid = f_form.find('input', {'name': 'bid'})['value']
            attack_key = f_form.find('input', {'name': 'attack_key'})['value']
            def_key = f_form.find('input', {'name': 'def_key'})['value']
            fightit = f_form.find('input', {'name': 'fightit'})['value']
            fightvl = f_form.find('input', {'name': 'fightvl'})['value']
            if f_form.find('a', id='left_attack1'):
            	left_attack = random.choice([1,2,3])
            else:
            	left_attack=0
            right_attack = random.choice([1,2,3])
            defence = random.choice([1,2,3])
            
            if f_form.find('a', id='walkbutton'):
            	walk = 1
            else:
            	walk=0
            enemy = 1

            url_atack = f'https://www.gwars.ru/b0/b.php?turn={turn}&bid={bid}&left_attack={left_attack}&right_attack={right_attack}&defence={defence}&attack_key={attack_key}&def_key={def_key}&walk={walk}&enemy={enemy}'
            url_atack_page = session.get(url_atack)
            print('Провел атаку')

            time.sleep(3)
            return fight()
    else:
        print('Бой окончен')
        
def ready_boi():
	a=session.get(url+url_boi)
	sa=BeautifulSoup(a.text, 'lxml')
	aa=sa.find('div', class_='greenbg_div')
	bb=aa.text.split('[')[1].split(']')[0].split('/')
	if bb[0]==bb[1]:
		print('I am ready!!!')
	else:
		print('Я очень слаб, не дай мне умереть =(')
		
async def find_zayavka():
	pass
	
async def cansel():
	pass