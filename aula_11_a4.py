"""
Botão final - all
"""

from selenium.webdriver import Firefox
from selenium.webdriver.common.alert import Alert
from time import sleep

b = Firefox()
url = 'https://selenium.dunossauro.live/aula_11_a'

b.get(url)
sleep(10)

b.find_element_by_id('all').click()
alerta = Alert(b)

# Note que aqui vou usar só um Alert para diferentes tipos de alerta

alerta.accept()             # alerta
alerta.send_keys('Pedro')   # prompt
alerta.accept()             # prompt
alerta.accept()             # confirma
