"""
Antes e depois são conhecidos como Hooks
EventListener: função -> observar o estado do web driver em todos os momentos.
Antes e depois de uma ação ser executada. Por exemplo, todas as vezes em que o 'click'
for chamado podemos observar o estado do dom, de um único elemento, fazer logs, etc.
"""


"""
Event firing
É uma "burocracia" do Selenium para utilizar um Listener
Criar um wrapper ('invólucro') para o webdriver e disparar os elementos para o Listener
"""

from selenium.webdriver import Firefox
from selenium.webdriver.support.events import (AbstractEventListener, EventFiringWebDriver)
from time import sleep

b = Firefox()

class Escuta(AbstractEventListener):
    def after_navigate_to(self, url, webdriver):
        print(f'Indo para {url}')

    def after_navigate_back(self, webdriver):
        print('Voltando para a página anterior')

    def before_click(self, elemento, webdriver):
        if elemento.tag_name == 'input':
            print(webdriver.find_element_by_tag_name('span').text)
        print(f'Antes do clique no {elemento.tag_name}')

    def after_click(self, elemento, webdriver):
        print(f'Depois do clique no {elemento.tag_name}')
        if elemento.tag_name == 'input':
            print(webdriver.find_element_by_tag_name('span').text)


# Note que tudo aquilo que fazíamos antes com "b" (browser), passamos a fazer com "wrapper_b" (wrapper do browser)
wrapper_b = EventFiringWebDriver(b, Escuta())  # wrapper, por favor faça o link entre o browser e a Escuta
wrapper_b.get('https://selenium.dunossauro.live/aula_07_d')

sleep(10)

input_texto = wrapper_b.find_element_by_tag_name('input')
span = wrapper_b.find_element_by_tag_name('span')

input_texto.click()
span.click()

wrapper_b.get('https://selenium.dunossauro.live/aula_07_c')
wrapper_b.back()

wrapper_b.quit()
