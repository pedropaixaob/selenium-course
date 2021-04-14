"""
ROTEIRO

- Alertas: alertas, confirmações e prompts (11a1)
- Janelas e Abas (11b)
- iFrames (11c)
"""

"""
ALERTAS
-------
Alertas são elementos relativos às janelas.
São elementos que não necessariamente estão presentes no DOM.
b.switch_to.alert retorna objeto

OBS: Posso dar switch_to para outros locais: .window, .frame, etc.

Métodos que podem ser utilizados: accept, dismiss, send_keys, text
"""

from selenium.webdriver import Firefox
# from selenium.webdriver.common.alert import Alert
from time import sleep

b = Firefox()
url = 'https://selenium.dunossauro.live/aula_11_a'

b.get(url)
sleep(10)
b.find_element_by_id('alert').click() # Clica no botão de id 'alert'

alerta = b.switch_to.alert
print(alerta.text)

# alerta = Alert(b)
# Ao invés de usar switch_to, poderíamos usar o Alert Quando usamos Alert,
# não precisamos necessariamente o alerta precisa estar mostrado na tela
# para conseguir capturar o objeto. Uma vez capturado, ele continua lá,
# não precisando ser reacessado toda vez. Abordagens diferentes!

sleep(10)
alerta.accept() # Confirma, clica no OK
# alerta.dismiss() # Confirma, clica no OK
