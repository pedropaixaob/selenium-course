"""
1. Pegar todos os links de aulas
    {'nome da aula': 'link da aula'}
2. Navegar até o exercício 3
    achar a url do exercício 3 e ir até lá
"""
from selenium.webdriver import Firefox
from time import sleep
from pprint import pprint

browser = Firefox()
url = 'http://selenium.dunossauro.live/aula_04.html'
browser.get(url)

"""
Parte 1
"""

sleep(5)

def get_links(browser, elemento):
    """
    Pega todos os links dentro de um elemento
    - browser: instância de um navegador
    - elemento: web element (aside, main, body, ul, ol, etc.)
    e retorna um dicionário
    """
    element = browser.find_element_by_tag_name(elemento)
    element_ancoras = element.find_elements_by_tag_name('a')

    resultado = {}
    for ancora in element_ancoras:
        resultado[ancora.text] = ancora.get_attribute('href')

    return resultado

"""
Parte 1
"""
aulas = get_links(browser, 'aside')
pprint(aulas)

"""
Parte 2
"""

exercicios = get_links(browser, 'main')
link_exercicio_3 = exercicios['Exercício 3']
browser.get(link_exercicio_3)

# browser.refresh()
# browser.title()
# browser.current()
