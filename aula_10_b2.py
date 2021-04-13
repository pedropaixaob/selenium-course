"""
Usando located ao invés de element
"""

from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import (
visibility_of_element_located,
invisibility_of_element_located,
visibility_of_any_elements_located,
visibility_of_all_elements_located
)

url = 'https://selenium.dunossauro.live/aula_10_b.html'
b = Firefox()
b.get(url)

wdw = WebDriverWait(b, 60)

locator = (By.TAG_NAME, 'h1') # Se eu quisesse colocar qualquer tag, seria só trocar h1 por *

# Existência do elemento
wdw.until(visibility_of_element_located(locator),
'h1 não foi encontrado na página, com uma espera de 60s') # Por elemento, não por locator
print ('h1 disponível!')
