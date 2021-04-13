"""
Expected conditions

São classes prontas para esperas "comuns" (usuais).
Algumas categorias (não-oficiais) de espera:

- Existência do elemento: saber se o elemento está na tela, ou existe na tela
- Visibilidade do elemento:  saber se o elemento está desenhado na tela ou não, e também se ele está ativo ou não
- Navegação
- Verificação de texto

"""

from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located

url = 'https://selenium.dunossauro.live/aula_10_a.html'
b = Firefox()
b.get(url)

wdw = WebDriverWait(b, 30)
locator = (By.CSS_SELECTOR, '#request')

# Existência do elemento
wdw.until(presence_of_element_located(locator))
print ('Apareceu o request!')
b.find_element(*locator).click()
