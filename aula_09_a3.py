from functools import partial
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait

# Melhorando o código anterior
# O partial vai permitir que criemos uma função intermediária

def esperar_elemento(elemento, webdriver):
    elements = webdriver.find_elements_by_css_selector(elemento)
    print(f'Tentando encontrar {elemento}')
    return bool(elements)

# Funções intermediárias criadas a partir do "molde" espera_elemento
# Criamos uma nova função mais simples, fixando um parâmetro da função principal
esperar_botao = partial(esperar_elemento, 'button')
esperar_sucesso = partial(esperar_elemento, '#finished')

url = 'https://selenium.dunossauro.live/aula_09_a'
b = Firefox()
wdw = WebDriverWait(b, 10) # segundos

b.get(url)

wdw.until (esperar_botao, 'Deu ruim')
b.find_element_by_tag_name('button').click()
wdw.until (esperar_sucesso, 'A mensagem de sucesso não apareceu')
sucesso = b.find_element_by_css_selector('#finished')
assert sucesso.text == 'Carregamento concluído'
