"""

Esse scrapper possui a função de obter os seguidores de todos os participantes do BBB21

"""

from selenium.webdriver import Firefox
from datetime import datetime as dt
from time import sleep
import pandas as pd

instas = {'Arthur':'arthurpicoli',
          'Bil':'bilaraujjo', 
          'Caio':'afiune_caio',
          'Carla':'carladiaz',
          'Camilla':'camilladelucas',
          'Fiuk':'fiuk',
          'Gil':'gilnogueiraofc',
          'João':'joaolpedrosa',
          'Julliette':'juliette.freire',
          'Kerline':'kercardoso',
          'Lucas':'lucaskokapenteado',
          'Lumena':'lumena.aleluia',
          'Karol':'karolconka',
          'Nego Di':'negodioficial',
          'Pocah': 'pocah',
          'Projota':'projota',
          'Rodolffo':'irodolffo',
          'Sarah':'sarah_andrade',
          'Thais': 'thaisbraz',
          'Viih Tube':'viihtube'}

browser = Firefox()
followers_list = []

for brother, insta in instas.items():
    browser.get(f'http://instagram.com/{insta}/')
    followers = browser.find_elements_by_css_selector('.g47SY')[1].get_attribute('title')
    print(f'{brother} ({insta}) está com {followers} followers em {dt.now()}')
    followers_list.append(followers)

data_bbb = pd.DataFrame(
           [[dt.now()] + followers_list],
           columns=['data', *instas.keys()])

print(data_bbb)

browser.quit()