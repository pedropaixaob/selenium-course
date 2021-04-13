"""
Usand staleness_of: saber se elemento está habilitado/desabilitado
"""

from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
staleness_of
)

url = 'https://selenium.dunossauro.live/aula_10_b.html'
b = Firefox()
b.get(url)

wdw = WebDriverWait(b, 60)

# Staleness_of retorna se o elemento está ativo (is_enabled(elemento) = True) ou inativo (is_enabled(elemento) = False)
# Obs: notar diferença entre is_enabled (ativo/inativo) e is_displayed (escrito na tela)
wdw.until(staleness_of(
b.find_element_by_tag_name('button')),
'Button não foi habilitado na página, com uma espera de 60s') # Por elemento, não por locator
print ('Button está habilitado')

elemento.click()

p = browser.find_element_by_tag_name('p')

assert 'quei' in p.text

# Desafio futuro: implementar staleness_of com locator (simples)
