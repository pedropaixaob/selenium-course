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

browser = Firefox()
url = 'http://selenium.dunossauro.live/aula_04_b.html'
browser.get(url)

sleep(5)

nomes_das_caixas = ['um','dois','tres','quatro']

for nome in nomes_das_caixas:
    find_by_text(browser, 'div', nome).click()

for nome in nomes_das_caixas:
    sleep(0.3)
    browser.back()

for nome in nomes_das_caixas:
    sleep(0.3)
    browser.forward()

# browser.current_url()
