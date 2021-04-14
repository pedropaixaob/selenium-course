
"""
PROMPT
-------
Basicamente um booleano (janela de confirmação com "sim" ou "não")
"""

from selenium.webdriver import Firefox
from selenium.webdriver.common.alert import Alert
from time import sleep

b = Firefox()
url = 'https://selenium.dunossauro.live/aula_11_a'

b.get(url)
sleep(10)
b.find_element_by_id('confirm').click() # Clica no botão de id 'alert'

confirm = Alert(b)
print(confirm.text)

sleep(10)
confirm.accept() # Aperta em OK
# prompt.dismiss() # Aperta em Cancelar

# OBS: Posso dar switch_to para outros locais: .window, .frame, etc.
