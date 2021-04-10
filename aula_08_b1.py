"""
ActionChains - Mouse

.click
.click_and_hold
.context_click (é aquele que abre o menu, botão direito pra quem é destro)
.double_click

Tipos de eventos disparados pelo teclado

mouseenter
mouseleave
click
dblclick
contextmenu

obs: mouseenter + mouseleave = move_to_element

Atributos de ação
shiftKey
altKey
metaKey
ctrlKey

"""

# low_level.move_to_element(<WebElement1>)

from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

url = 'https://selenium.dunossauro.live/caixinha'
browser = Firefox()
browser.get(url)
browser.set_window_size(1404, 936)

caixa = browser.find_element_by_id('caixa')
span = browser.find_element_by_tag_name('span') # quando quisermos desfocar

ac = ActionChains(browser)

def caixinha_colorida(key1, key2=None): # colocamos a key2 para dar a oportunidade de apertar dois botões ao mesmo tempo

    ac.pause(1)
    ac.key_down(key1)
    if key2:
        ac.key_down(key2)
    ac.move_to_element(caixa)
    ac.pause(1)
    ac.click()
    ac.pause(1)
    ac.double_click()
    ac.pause(1)
    ac.move_to_element(span)
    if key2:
        ac.key_up(key2)
    ac.key_up(key1)

caixinha_colorida(Keys.SHIFT)
caixinha_colorida(Keys.CONTROL)
caixinha_colorida(Keys.CONTROL, Keys.SHIFT)

ac.move_to_element(caixa)
ac.context_click()
ac.pause(1)
ac.perform()
