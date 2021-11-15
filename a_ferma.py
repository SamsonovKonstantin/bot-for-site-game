from bs4 import BeautifulSoup

import a_login
import a_capcha


session=a_login.session

url='https://www.gwars.ru'
url_f='/ferma.php?'
nohead = '&nohead=1'

def find_button(id_plant):
	info_page = session.get(url+url_f) #потом перебрать все Х и У
	a_capcha.ferm(info_page)
	soup_info_page = BeautifulSoup(info_page.text,'lxml')
	try:
		posad=soup_info_page.find('input',{'name':'plantbutton'})['onclick'][9:-3]
		print('Посадить')
		print(posad)
		ferm_page=session.get(url+posad+'&plant_id='+id_plant+nohead)
		a_capcha.ferm(ferm_page)
	except:
		try:
			knopka = soup_info_page.find_all('a')
			for kn in knopka:
				if kn.text.split(' ')[0]=='Полить':
					sss=kn['href']
					print('Полить')
					print(url+sss)
					ferm_page=session.get(url+sss+nohead)
					a_capcha.ferm(ferm_page)
					return find_button(id_plant)
				elif kn.text.split(' ')[0]=='Вскопать':
					sss=kn['href']
					print('Вскопать')
					print(url+sss)
					ferm_page=session.get(url+sss+nohead)
					a_capcha.ferm(ferm_page)
					return find_button(id_plant)
				elif kn.text.split(' ')[0]=='Собрать':
					sss=kn['href']
					print('Собрать')
					print(url+sss)
					ferm_page=session.get(url+sss+nohead)
					a_capcha.ferm(ferm_page)
					return find_button(id_plant)
		except:
			print('Что-то пошло не так')
		print('Пока рано что-либо делать')
	
	
