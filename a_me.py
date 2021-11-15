from bs4 import  BeautifulSoup

import a_login


url=a_login.url
sesion=a_login.session

def me():
	try:
		url_me = '/me.php'
		me_page=sesion.get(url+url_me)
		soup_me_page= BeautifulSoup(me_page.text, 'lxml')
		tds=soup_me_page.find_all('td', colspan='2')
		print(tds[1].text)
		tda=tds[2].find_all('td')
		print(tda[0].text)
	except:
		print("Нет возможности получить инфо, т.к. вы находитесь в пути")
	

	