import time

import a_login
import a_me
import a_map
import a_boi
import a_trade
import a_ferma


l=input('Введете логин: ')
p=input('Введете пароль: ')

res='weed' #metal uran weed solomka
sell_cost=31 #27 103 32 34
buy_cost=31 #26 102 31 33
babki=0
count_pages = 5

id_plant='opyata'

a_login.login(l,p)
a_me.me()
x,y=a_map.start_position()
a_map.info_map()

a_boi.ready_boi()

while True:
    a_trade.sell_object(res,sell_cost,buy_cost,babki,count_pages)
    print('Перерыв')
    time.sleep(300)
    #a_map.move_map(x,y)
    a_ferma.find_button(id_plant)

