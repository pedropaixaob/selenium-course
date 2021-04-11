from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait

def esperar_botao(webdriver):
    """Verifica se o elemento 'button' está na tela."""
    elements = webdriver.find_elements_by_css_selector('button')
    print('Tentando encontrar "button"')
    return bool(elements) # Se lista vazia, bool = False. c.c., bool=True
    # Atenção! A função que jogarmos no until deve retornar True ou False

def esperar_sucesso(webdriver):
    """Verifica se o elemento de id 'finished' está na tela."""
    elements = webdriver.find_elements_by_css_selector('#finished')
    print('Tentando encontrar "finished"')
    return bool(elements) # Se lista vazia, bool = False. c.c., bool=True
    # Atenção! A função que jogarmos no until deve retornar True ou False

url = 'https://selenium.dunossauro.live/aula_09_a'
b = Firefox()
wdw = WebDriverWait(b, 10) # segundos

b.get(url)

# Esperar botão
# Vai retornar 'Deu ruim' se não conseguir encontrar a tempo
wdw.until (esperar_botao, 'Deu ruim') # Atenção! Aqui passamos só a função, não precisa nem o argumento!

# Clicar no botão
b.find_element_by_tag_name('button').click()

# Esperar sucesso
# Vai retornar mensagem se não conseguir encontrar a tempo
wdw.until (esperar_sucesso, 'A mensagem de sucesso não apareceu')

sucesso = b.find_element_by_css_selector('#finished')
assert sucesso.text == 'Carregamento concluído'
