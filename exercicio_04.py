from selenium.webdriver import Firefox
from time import sleep
from urllib.parse import urlparse
from json import loads # transformar estrutura de json e transformar em dicionário

browser = Firefox()
url = 'http://selenium.dunossauro.live/exercicio_04.html'
browser.get(url)

def preenche_form(browser, nome, email, senha, telefone):
    browser.find_element_by_name('nome').send_keys(nome)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('senha').send_keys(senha)
    browser.find_element_by_name('telefone').send_keys(telefone)
    sleep(5)
    browser.find_element_by_id('btn').click()


"""
PARTE 1 - OBTÉM DICIONÁRIO DO textarea
"""

sleep(5)
preenche_form(browser, 'Pedro', 'pedro@pedromail.com', 'senha123', '(021)2222-2222')
sleep(5)
texto_resultado = browser.find_element_by_tag_name('textarea').text
resultado_arrumado = texto_resultado.replace('\'', "\"") # não estava conseguindo ler aspa simples, então trocamos por aspas duplas.
dict_result = loads(resultado_arrumado)

"""
PARTE 2 - OBTÉM DADOS DA URL
"""

dict_url = {}
url_parseada = urlparse(browser.current_url)
texto_url = url_parseada.query.split('&')
for item in texto_url[0:4]:
    item_name, item_response = item.split('=')

    # tratamento dos parênteses e @
    dict_correcao = {'%40': '@', '%28': '(', '%29': ')'}
    for i, j in dict_correcao.items():
        item_response = item_response.replace(i,j)

    dict_url[item_name] = item_response


"""
PARTE 3 - CONFERINDO OS DICIONÁRIOS OBTIDOS SÃO, DE FATO, IGUAIS
"""
assert dict_result == dict_url
