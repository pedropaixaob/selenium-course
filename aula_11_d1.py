"""
iFrame: página dentro de outra página
Não consigo acessar um elemento dentro do iFrame diretamente do DOM geral,
tenho que acessar primeiro o DOM do iFrame

browser.switch_to_frame

Wait de iFrame: frame_to_be_available_and_switch_to_it

"""

from selenium.webdriver import Firefox
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
frame_to_be_available_and_switch_to_it,
element_to_be_clickable
)

b = Firefox()
wdw = WebDriverWait(b, 60)

url = 'https://selenium.dunossauro.live/aula_11_d'
b.get(url)

# Aqui não conseguiria rodar b.find_element_by_id('nome'), pois o elemento está dentro do iFrame

# frame_to_be_available_and_switch_to_it recebe locator
wdw.until(frame_to_be_available_and_switch_to_it(('name', 'iframe'))) # Todo iFrame tem um nome! O nome desse é iFrame
wdw.until(element_to_be_clickable(('name','nome'))) # Espera o campo 'nome' estar clicável
b.find_element_by_id('nome').send_keys('Pedro')
b.find_element_by_id('email').send_keys('pedro@mail.com')
b.find_element_by_id('senha').send_keys('1234')
b.find_element_by_id('btn').click()
