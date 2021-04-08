
from selenium.webdriver import Firefox
from selenium.webdriver.support.events import (AbstractEventListener, EventFiringWebDriver)
from time import sleep

b = Firefox()

class Escuta(AbstractEventListener):

    def before_click(self, elemento, webdriver):
        nome_atributo = elemento.get_attribute('name')
        print(f'Antes do clique no {elemento.tag_name} de atributo {nome_atributo}')
        if elemento.tag_name == 'input':
            print(webdriver.find_element_by_css_selector(f'[for={nome_atributo}]').text)

    def after_click(self, elemento, webdriver):
        nome_atributo = elemento.get_attribute('name')
        print(f'Depois do clique no {elemento.tag_name} de atributo {nome_atributo}')
        if elemento.tag_name == 'input':
            print(webdriver.find_element_by_css_selector(f'[for={nome_atributo}]').text)

wrapper_b = EventFiringWebDriver(b, Escuta())

wrapper_b.get('https://selenium.dunossauro.live/exercicio_07.html') # Abre wrapper com browser
sleep(5)

input_nome, input_email, input_senha = wrapper_b.find_elements_by_tag_name('input')[:3]

input_nome.click()
input_nome.send_keys('Pedro') # Preenchendo o campo 'nome'
sleep(3)

input_email.click()
input_email.send_keys('pedro@meu-email.com') # Preenchendo o campo 'email'
sleep(3)

input_senha.click()
input_senha.send_keys('senha123') # Preenchendo o campo 'senha'
sleep(3)

button = b.find_elements_by_tag_name('input')[-1]  # Aqui não usei o wrapper, pois não queria o EventListener
button.click() # Enviando formulário

sleep(5)
wrapper_b.quit() # Fecha wrapper / browser
