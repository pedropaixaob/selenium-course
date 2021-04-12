"""
Por vezes, podemos ver o elemento, mas ele não tem
as características que precisamos para clicar (está inativo)

Para esperar o elemento ser ativado, podemos usar o método is_enabled
"""

from functools import partial
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

class EsperarElementoNotClick:
    def __init__(self, locator):
        self.locator = locator

    # Espera baseada em classe, olhando se o elemento está ativo ou não
    def __call__(self, webdriver):
      elementos = webdriver.find_elements(*self.locator)
      if elementos:
          return 'unclick' in elementos[0].get_attribute('class')
      return False

# Espera baseada em função
def esperar_elemento(by, elemento, webdriver):
  if webdriver.find_elements(by, elemento):
    return True
  return False

locator = (By.CSS_SELECTOR, 'button')
esperar_botao = EsperarElementoNotClick(locator)

url = 'https://selenium.dunossauro.live/aula_09_a'
b = Firefox()
wdw = WebDriverWait(b, 10) # segundos
b.get(url)

sleep(5)

wdw.until_not(esperar_botao, 'Não encontrou button') # Não quero que tenha o unclick na área do button

b.find_element_by_css_selector('button').click()

wdw.until(partial(esperar_elemento, 'id', 'finished'), 'Não encontrou finished')

sucesso = b.find_element_by_css_selector('#finished')

assert sucesso.text == 'Carregamento concluído'
