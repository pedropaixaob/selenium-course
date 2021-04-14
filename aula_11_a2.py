
"""
PROMPT
-------
Aparece um texto, um campo a ser preenchido,
e dois botões "OK" (accept) e "Cancelar" (dismiss)

Prompt é tratado como alerta
"""

from selenium.webdriver import Firefox
from selenium.webdriver.common.alert import Alert
from time import sleep

b = Firefox()
url = 'https://selenium.dunossauro.live/aula_11_a'

b.get(url)
sleep(10)
b.find_element_by_id('prompt').click() # Clica no botão de id 'alert'

prompt = Alert(b)
prompt.send_keys('Pedro')
print(prompt.text)

sleep(10)
prompt.accept() # Aperta em OK
# prompt.dismiss() # Aperta em Cancelar

# OBS: Posso dar switch_to para outros locais: .window, .frame, etc.
