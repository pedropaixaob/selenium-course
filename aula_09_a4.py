"""
by nos auxilia a deixar o código mmais assertivo.
Ele é comumente utilizado em conjunto com o 'wb.find_element'
Mais um nível de parametrização!
"""
from functools import partial
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def esperar_elemento(by, elemento, web_driver):
    """Concatena o by com o elemento a ser buscado."""
    print(f'Tentando encontrar "{elemento}" by "{by}"')
    if web_driver.find_elements(by, elemento):
        return True
    return False

esperar_botao = partial(esperar_elemento, By.CSS_SELECTOR, 'button')
esperar_sucesso = partial(esperar_elemento, By.ID, 'finished')

url = 'https://selenium.dunossauro.live/aula_09_a'
b = Firefox()
wdw = WebDriverWait(b, 30) # segundos

b.get(url)

wdw.until (esperar_botao, 'Deu ruim')
b.find_element_by_tag_name('button').click()

wdw.until (esperar_sucesso, 'A mensagem de sucesso não apareceu')
sucesso = b.find_element_by_css_selector('#finished')

assert sucesso.text == 'Carregamento concluído'
