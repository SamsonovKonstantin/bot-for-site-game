#pylint:disable=W0611
#pylint:disable=E0401
import pickle
import requests
import lxml
import time

from bs4 import BeautifulSoup
from threading import Timer


HEADERS={
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

session = requests.Session()


URL1 = 'https://www.gwars.ru/login.php'

res1=session.get(URL1, headers=HEADERS)
#print (res1.status_code)
#print(res1.text)
soup1 = BeautifulSoup(res1.text,'lxml')
#print (soup1.findAll("input", {"name" : "loginkey"}))
loginkey1 =  soup1.find("input", {"name" : "loginkey"})['value']
loginkeymd1 = soup1.find("input", {"name" : "loginkeymd"})['value']
#print(res1.cookies)

EN = ['41', '42', '43', '44', '45', '46', '47', '48', '49',
          '4A', '4B', '4C', '4D', '4E', '4F',
          '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '5A',
          '61', '62', '63', '64', '65', '66', '67', '68', '69',
          '6A', '6B', '6C', '6D', '6E', '6F',
          '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '7A',
          '30', '31', '32', '33', '34', '35', '36', '37', '38', '39']

def loo():
    loogin = ('Мастер К') #input('Введите логин: ')
    l=[]
    t=0
    for i in loogin:
        if i == ' ':
            i = '+'
            l.append(i)
        elif i.encode("windows-1251").hex().upper() in EN:
            l.append(i)
        else:
            l.extend(['%',loogin[t].encode("windows-1251").hex().upper()])
        t= t+1
    return ''.join(l)

def paa():
    paassword = ('warest13') #input('Введите пароль: ')
    p = []
    t = 0
    for i in paassword:
        if i == ' ':
            i = '+'
            p.append(i)
        elif i.encode("windows-1251").hex().upper() in EN:
            p.append(i)
        else:
            p.extend(['%', paassword[t].encode("windows-1251").hex().upper()])
        t = t + 1
    return ''.join(p)

def vhod():
    URL2 = f'https://www.gwars.ru/login.php?loginkey={loginkey1}&loginkeymd={loginkeymd1}&login={loo()}&pass={paa()}&store_password_here=1'

    res2=session.post(URL2, headers=HEADERS)
    #print (res2.status_code)

    soup2 = BeautifulSoup(res2.text,'lxml')
    try:
        if soup2.find("input", {"id" : "gotobutton"})['value']=='Войти':
            vhod()
    except:
        pass


    loc_map = session.get('https://www.gwars.ru/map.php', headers=HEADERS)

    with open("index.html", 'w', encoding = (loc_map.encoding) ) as file:
        file.write(loc_map.text)

vhod()
print ('The End')

#куда продать
def sale_objects():
    s=0
    USOs = []
    while s<1:
    	sURL = (f'https://www.gwars.ru/statlist.php?r=uran&page_id1={s}')
    	print(sURL)
    	sale_page = session.post(sURL)
    	soup_sale_page = BeautifulSoup(sale_page.text,'lxml')
    	uran_object = soup_sale_page.find_all(class_ ='withborders')
    	stors_s = uran_object[0].find_all('tr')
    	for stor_s in stors_s:
         	if stor_s.find_all('a',style="color:#ff0404;font-weight:bold;"):
         	       USO = stor_s.find_all('a')[1].get('href')
         	       USOs.append(USO)
    	s=s+1
    return USOs, print(USOs)
         	      
    
sale_objects()

#продажа в магаз

def sale(USOs):
    url = 'https://www.gwars.ru'
    try:

        for USO in USOs:
                sale_store_page = session.get(url+USO)
                soup_sale_store = BeautifulSoup(sale_store_page.text,'lxml')
                objs_pars = soup_sale_store.find_all('table')
                resurses = objs_pars[9].find_all('tr')
                
                

                for resurs in resurses[3:(len(resurses) - 1)]:

                    res = resurs.find_elements_by_tag_name('td')

                    # print(len(res))

    #                try:

                    if res[0].text == 'Уран':

                        i_res = res[4].text

                        if int(i_res[1:]) > (101):

                            if int(res[6].text) > (0):

                                try:

                                    driver.find_element_by_id("uran_sellform").find_element_by_class_name('mainbutton').click()

                                    print('продажа')

                                    #print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

                                except:

                                    time.sleep(2)

                            else:

                                buy(buy_object())

    #                except:

                    time.sleep(3)

    except:

        time.sleep(2)



