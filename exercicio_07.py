
from selenium.webdriver import Firefox
from selenium.webdriver.support.events import (AbstractEventListener, EventFiringWebDriver)
from time import sleep

b = Firefox()

class Escuta(AbstractEventListener):

    def before_click(self, elemento, webdriver):
        nome_atributo = elemento.get_attribute('name')
        print(f'Antes do clique no {elemento.tag_name} de atributo {nome_atributo}')
        if elemento.tag_name == 'input':
            print(webdriver.find_element_by_tag_name('label').text)

    def after_click(self, elemento, webdriver):
        nome_atributo = elemento.get_attribute('name')
        print(f'Depois do clique no {elemento.tag_name} de atributo {nome_atributo}')
        if elemento.tag_name == 'input':
            print(webdriver.find_element_by_tag_name('label').text)

wrapper_b = EventFiringWebDriver(b, Escuta())

wrapper_b.get('https://selenium.dunossauro.live/exercicio_07.html') # Abre wrapper com browser
sleep(5)

input_nome, input_email, input_senha, input_btn = wrapper_b.find_elements_by_tag_name('input')

input_nome.click()
input_nome.send_keys('Pedro') # Preenchendo o campo 'nome'
sleep(3)

input_email.click()
input_email.send_keys('pedro@meu-email.com') # Preenchendo o campo 'email'
sleep(3)

input_senha.click()
input_senha.send_keys('senha123') # Preenchendo o campo 'senha'
sleep(3)

input_btn.click() # Enviando formulário

wrapper_b.quit() # Fecha wrapper / browser
