# forms: target, action, method
# target: para onde iremos redirecionar a página (_self - mesma janela, _blank - abre outra janela)
# method: protocolo/verbos HTTP (get (envio na URL) , post (envio por requisição da web, não vemos esses dados) , etc.)
# action: se vamos carregar outra URL (URL) ou fazer na própria página (#)

from selenium.webdriver import Firefox
from time import sleep
from urllib.parse import urlparse
from json import loads # transformar estrutura de json e transformar em dicionário

browser = Firefox()
url = 'http://selenium.dunossauro.live/aula_05.html'
browser.get(url)

sleep(5)

def preenche_form(browser, nome, email, senha, telefone):
    browser.find_element_by_name('nome').send_keys(nome)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('senha').send_keys(senha)
    browser.find_element_by_name('telefone').send_keys(telefone)
    sleep(5)
    browser.find_element_by_name('btn').click()

# browser.current_url
# ? query string
''' https://selenium.dunossauro.live/aula_05.html?
nome=Pedro
&
email=pedro%40email.com.br
&
senha=senhadopedro
&
telefone=%2821%292222-2222
&
btn=Enviar%21#
'''



preenche_form(browser, 'Pedro', 'pedro@email.com.br', 'senhadopedro', '(21)2222-2222')

sleep(5)

estrutura = {'nome': 'Pedro', 'email': 'pedro@email.com.br', 'senha': 'senhadopedro', 'telefone': '(21)2222-2222'}

# url_parseada = urlparse(browser.current_url)
# Poderíamos fazer simplesmente url_parseada.query.split('&') para obter a lista com os splits
# No entanto, nessa página, a div "resultado" já retorna um dicionário de forma direta
# Vamos testar se o resultado gerado é o esperado

texto_resultado = browser.find_element_by_id('result').text
resultado_arrumado = texto_resultado.replace('\'', "\"") # não estava conseguindo ler aspa simples, então trocamos por aspas duplas.
dict_result = loads(resultado_arrumado)

sleep(5)
assert dict_result == estrutura
browser.quit()
