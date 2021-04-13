"""
Visibilidade do elemento: possível checar visível/invisível ou ativo/inativo
Visível/invisível está no CSS, ativo/inativo está no HTML
"""

from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import(
visibility_of, invisibility_of_element)

url = 'https://selenium.dunossauro.live/aula_10_b.html'
b = Firefox()
b.get(url)

wdw = WebDriverWait(b, 60)
elemento = b.find_element_by_tag_name('h1')

# Existência do elemento
wdw.until(visibility_of(elemento),
'h1 não foi encontrado na página, com uma espera de 60s') # Por elemento, não por locator
print ('h1 disponível!')
