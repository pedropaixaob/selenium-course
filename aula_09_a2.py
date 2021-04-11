"""
WAITS EXPLÍCITOS

- Selenium disponibiliza um range de waits prontos
- Customizável
- Reutilizável

wdw = WebDriverWait(
    driver, #Webdriver
    timeout, #Tempo de espera até o erro
    poll_frequency=0.5, # Tempo de espera entre uma tentativa e outra
    ignored_exceptions=None # Lista de coisas que vamos ignorar
    )

### UNTIL
Exercuta até que o 'Callable' retorne True, ou até estourar o 'timeout' de wdw
wdw.until(
    Callable # Operação que vai ser executada
    message # Mensagem caso o erro ocorra
    )

    Callable vai ficar sendo chamado no tempo do pooling (pool_frequency)
    'O elemento já tá pronto?' 'O elemento já tá pronto?'
    'O elemento já tá pronto?' 'O elemento já tá pronto?'
    Esperar até que retorne True

wdw.until(função)

### NOT_UNTIL
Exercuta até que o 'Callable' retorne False, ou até estourar o 'timeout' de wdw
wdw.not_until(
    Callable # Operação que vai ser executada
    message # Mensagem caso o erro ocorra
    )

"""

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
