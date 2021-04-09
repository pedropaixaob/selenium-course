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

url = https://selenium.dunossauro.live/caixinha
b.get(url)
