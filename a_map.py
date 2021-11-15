import time
import random

from bs4 import BeautifulSoup

import a_login
import a_capcha


session=a_login.session

url_map='https://www.gwars.ru/map.php'

def start_position():
    loc_map = session.get(url_map)
    soup_loc_map = BeautifulSoup(loc_map.text, 'lxml')
    a_capcha.figth(url_map)
    if soup_loc_map.find('div', id='mmdiv'):
        move = soup_loc_map.find('div', id='mmdiv')
        print(f'Please wait {int(move.text) + 5}sec, you move in next location.')
        time.sleep(int(move.text) + 5)
    loc_map = session.get(url_map)
    soup_loc_map = BeautifulSoup(loc_map.text, 'lxml')
    a_capcha.figth(url_map)
    my_pos = soup_loc_map.find('a',class_='nul')['href'].split('=')
    sy=int(my_pos[2])
    sx=int(my_pos[1].split('&')[0])
    tx = [0, 1, 2, 3, 4, 5, 6]
    ty = [0, 1, 2, 3, 4, 5, 6]
    atx=random.choice([tx[::-1],tx])
    aty=random.choice([ty[::-1],ty])
    ix = sx - 47
    iy = sy - 47
    x = atx[ix:] + atx[6:6 - ix:-1]
    y = aty[iy:] + aty[6:6 - iy:-1]
    return x,y
 
def info_map():
    mapp = session.get(url_map)
    soup_mapp=BeautifulSoup(mapp.text, 'lxml')
    if soup_mapp.find('div', id='mmdiv'):
        move =soup_mapp.find('div', id='mmdiv')
        print(f'Please wait {int(move.text)+5}sec, you move in next location.')
        time.sleep(int(move.text)+5)
        a_capcha.figth(url_map)
    else:
        print ("Вы находитесь не в движении")

def move_map(x,y):
    if x[0]<x[1]:
        x.append(abs(x[0]-6))
        del x[0]
        mapp=session.get('https://www.gwars.ru/map.move.php?moveright=1')
        info_map()
    elif x[0] > x[1]:
        x.append(abs(x[0] - 6))
        del x[0]
        mapp=session.get('https://www.gwars.ru/map.move.php?moveleft=1')
        info_map()
    else:
        if y[0]<y[1]:
            x.append(abs(x[0] - 6))
            del x[0]
            y.append(abs(y[0] - 6))
            del y[0]
            mapp =session.get('https://www.gwars.ru/map.move.php?movedown=1')
            info_map()
        elif y[0]>y[1]:
            x.append(abs(x[0] - 6))
            del x[0]
            y.append(abs(y[0] - 6))
            del y[0]
            mapp=session.get('https://www.gwars.ru/map.move.php?moveup=1')
            info_map()
        else:
            x.append(abs(x[0] - 6))
            del x[0]
            y.append(abs(y[0] - 6))
            del y[0]
    print(x, y)
    print('next local')
    return x,y
    