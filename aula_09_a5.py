"""
Abordagem similar, utilizando OO
Evitar uso do partial: '__call__'
Abordagem tradicional, não necessariamente a melhor (depende do contexto)
"""

from functools import partial
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class EsperarElemento:
    def __init__(self, locator):
        # Locator é uma tupla do By com a string do Elemento
        self.locator = locator

    def __call__(self, webdriver):
        if webdriver.find_elements(*self.locator):
            return True
        return False

locator_1 = (By.CSS_SELECTOR, 'button')
locator_2 = ('id', 'finished') # posso usar só a string ao invés do by

url = 'https://selenium.dunossauro.live/aula_09_a'
b = Firefox()
wdw = WebDriverWait(b, 30) # segundos

b.get(url)

wdw.until(EsperarElemento(locator_1), 'Não encontrou button')
b.find_element_by_css_selector('button').click()
wdw.until(EsperarElemento(locator_2), 'Não encontrou finished')
sucesso = b.find_element_by_css_selector('#finished')

assert sucesso.text == 'Carregamento concluído'
