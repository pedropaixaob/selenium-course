from selenium.webdriver import Firefox
from time import sleep

def find_by_text(browser, tag, text):
    """Encontrar o elemento com o texto 'text'

    Argumentos:
    - browser = Instância do browser (firefox, chrome...)
    - text = conteúdo que deve estar na tag
    - tag = onde o texto será procurado
    """

    elementos = browser.find_elements_by_tag_name(tag)  # lista

    for elemento in elementos:
        if elemento.text == text:
            return elemento

def find_by_href(browser, link):
    """Encontrar o elemento com o texto 'text'

    Argumentos:
    - browser = Instância do browser (firefox, chrome...)
    - link = link que será procurado em todas as tags 'a'
    Não precisamos especificar tag na função porque quase sempre o link está na tag 'a' (âncora)
    """

    elementos = browser.find_elements_by_tag_name('a')  # lista

    for elemento in elementos:
        if link in elemento.get_attribute('href'):
            return elemento

browser = Firefox()
url = 'http://selenium.dunossauro.live/aula_04_a.html'
browser.get(url)

sleep(5)

# elemento_ddg = find_by_text(browser, 'li', 'DuckDuckGo')
elemento_ddg = find_by_href(browser, 'ddg') # Qualquer link que contenha a expressão 'ddg'
