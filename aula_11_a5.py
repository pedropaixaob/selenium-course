"""
Wait específico para quando alert está presente
"""

from selenium.webdriver import Firefox
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present
from time import sleep

b = Firefox()
url = 'https://selenium.dunossauro.live/aula_11_a'
wdw = WebDriverWait(b, 30)

b.get(url)
sleep(10)

b.find_element_by_id('alertd').click()

print('Antes de esperar o alerta')
alerta = wdw.until(alert_is_present()) # Ao fazer o alert_is_present, nesse caso, já retorna o objeto
print('Depois de esperar o alerta')

# Outra opção
# alerta = Alert(b)
# wdw.until(alert_is_present()) # Esperar dar o tempo do alerta estar presente

alerta.accept()
