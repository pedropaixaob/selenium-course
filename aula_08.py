"""
Keyboard Events
- keyup
- keydown
- accesskey: atributo global (não vamos focar muito nele)

Vários atributos:
- key (valor da tecla)
- atributos de teclas (shiftKey, altKey, metaKey, ctrlKey)
- getModifierState() (caps lock, shift, meta, os)
"""

#from selenium.webdriver import Firefox
#url = 'https://selenium.dunossauro.live/keyboard'
#browser = Firefox()
#browser.get(url)

############## browser.send_keys('ABCDE') #### Atenção! Não dá pra fazer isso! Precisamos selecionar algum elemento.

#html = browser.find_element_by_tag_name('html')
#html.send_keys('ABCDE')

"""
ActionChains são maneiras de automatizar ações de baixo nível

Funções para o teclado:

- .key_down: segura a tecla
- .key_up: solta a tecla
- .send_keys
- .send_keys_to_element

"""

from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# IMPORTANTE !
# https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.keys

url = 'https://selenium.dunossauro.live/aula_08_a'
browser = Firefox()
browser.get(url)

texto = 'Selenium'

# Hi-level
elemento = browser.find_element_by_name('texto')
# elemento.send_keys(texto)

# Low-level

ac = ActionChains(browser)
ac.move_to_element(elemento)
ac.click(elemento)

def digita_com(key):

    ac.key_down(key) # Shift = u'\ue008'
    for letra in texto:
        ac.key_down(letra)
        ac.key_up(letra)
    ac.key_up(key)

digita_com(Keys.SHIFT)

ac.perform()
