from bs4 import  BeautifulSoup

import requests


session = requests.Session()

url='https://www.gwars.ru'

def log_pas(lp):
        EN = ['41', '42', '43', '44', '45', '46', '47', '48', '49',
          '4A', '4B', '4C', '4D', '4E', '4F',
          '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '5A',
          '61', '62', '63', '64', '65', '66', '67', '68', '69',
          '6A', '6B', '6C', '6D', '6E', '6F',
          '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '7A',
          '30', '31', '32', '33', '34', '35', '36', '37', '38', '39']
          
        lo = []
        t = 0
        for i in lp:
            if i == ' ':
                i = '+'
                lo.append(i)
            elif i.encode("windows-1251").hex().upper() in EN:
                lo.append(i)
            else:
                lo.extend(['%', lp[t].encode("windows-1251").hex().upper()])
            t = t + 1
        return ''.join(lo)


def login(l,p):
	login_page = session.get('https://www.gwars.ru/login.php')
	soup_login_page = BeautifulSoup(login_page.text, 'lxml')
	loginkey1 = soup_login_page.find("input", {"name": "loginkey"})['value']
	loginkeymd1 = soup_login_page.find("input", {"name": "loginkeymd"})['value']
	
	url_login = f'https://www.gwars.ru/login.php?loginkey={loginkey1}&loginkeymd={loginkeymd1}&login={log_pas(l)}&pass={log_pas(p)}&store_password_here=1'
	res2 = session.post(url_login)
	soup2 = BeautifulSoup(res2.text, 'lxml')
	try:
	               if soup2.find("input", {"id": "gotobutton"})['value'] == 'Войти':
	               	print('ewe raz')
	               	login(l,p)
	except:
            print("Успешный вход")


def ppp(n,s):
	with open('teg.txt', 'w',encoding='utf-8') as f:
		f.write(n.text)
	with open('noteg.txt', 'w',encoding='utf-8') as f:
		f.write(s.text)
