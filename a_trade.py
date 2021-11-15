import time

from bs4 import BeautifulSoup
from random import randint

import a_login
import a_capcha
import a_map


session = a_login.session
    
def sell_object(res,sell_cost,buy_cost,babki,n):
    s=0
    while s<n:
        sURL = (f'https://www.gwars.ru/statlist.php?r={res}&page_id1={s}')
        print (sURL)
        sell_page = session.get(sURL)
        soup_sell_page = BeautifulSoup(sell_page.text,'lxml')
        sell_stores = soup_sell_page.find_all(class_='withborders')
        stores_s = sell_stores[0].find_all('tr')
        for stor_s in stores_s:
            try:
                if stor_s.find_all('a',style="color:#ff0404;font-weight:bold;"):
                	id_obj = stor_s.find_all('a')[1].text[1:]
                	url0=f'https://www.gwars.ru/object.php?id={id_obj}'
                	page_obj=session.get(url0)
                	soup_page_obj = BeautifulSoup(page_obj.text,'lxml')
                	s_res_value = int(soup_page_obj.find('form', id=f'{res}_sellform').find('input', {'name':'amount'})['value'])
                	s_res_price= int(soup_page_obj.find('form', id=f'{res}_sellform').find('input', {'name':'checkprice'})['value'])
                	print(s_res_value,s_res_price)
                	if s_res_value == 0:
                			return buy_object(res,sell_cost,buy_cost,babki,n)
                	elif s_res_price >= sell_cost:
                			url=f'https://www.gwars.ru/object-transfers.php?id={id_obj}&resource={res}&checkprice={s_res_price}&action=sell&amount={s_res_value}'
                			trade_page = session.get(url)
                			babki=(s_res_value * (s_res_price - buy_cost) + babki)
                			print(url0)
                			a_capcha.capcha_find(trade_page,url0)
                			print(f'Продано {s_res_value} ед. по {s_res_price} $. Итого: {babki}')
                			time.sleep(randint(7,15))
                	else:
                			print('Так дешево не продаем, идем дальше')
                			return babki
            except:
            	continue
        s=s+1
    return babki
        
def buy_object(res,sell_cost,buy_cost,babki,n):
	b = 0
	UBOs = []
	while b < n:
		bURL = (f'https://www.gwars.ru/statlist.php?r={res}&page_id2={b}')
		print(bURL)
		buy_page = session.get(bURL)
		soup_buy_page = BeautifulSoup(buy_page.text, 'lxml')
		buy_stores = soup_buy_page.find_all(class_='withborders')
		stores_b = buy_stores[1].find_all('tr')
		for stor_b in stores_b:
			try:
				if stor_b.find_all('a',style="color:#ff0404;font-weight:bold;"):
					id_obj = stor_b.find_all('a')[1].text[1:]
					url0=f'https://www.gwars.ru/object.php?id={id_obj}'
					page_obj=session.get(url0)
					soup_page_obj = BeautifulSoup(page_obj.text,'lxml')
					buy_trades=soup_page_obj.find_all('form')
					for buy_trade in buy_trades:
						try:
							b_res_value=int(buy_trade.find('input',{'name':'amount'})['value'])
							b_res_price=int(buy_trade.find('input',{'name':'checkprice'})['value'])
							if buy_trade.find('input',{'name':'resource'})['value'] == res:
								if b_res_value == 0:
									continue
								elif b_res_price > buy_cost:
									print('Дорого покупать, идем дальше')
									return babki
								else:
									url=f'https://www.gwars.ru/object-transfers.php?id={id_obj}&resource={res}&action=buy&checkprice={b_res_price}&action1=buyr&amount={b_res_value}'
									babki=babki+(buy_cost-b_res_price)*b_res_value
									trade_page=session.get(url)
									print(url0)
									print(f'куплено {b_res_value} ед. по {b_res_price} $.')
									a_capcha.capcha_find(trade_page,url0)
									time.sleep(randint(7,15))
									return sell_object(res,sell_cost,buy_cost,babki,n)
						except:
							continue
			except:
				continue
		b=b+1
	return babki
        
