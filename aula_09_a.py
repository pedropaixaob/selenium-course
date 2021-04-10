"""
Waits

Dois tipos de espera
- Explícitas:
- Implícitas: espera todos os eventos, navegação, com um tempo padrão

browser.implicitly_wait(30)
"""

from selenium.webdriver import Firefox
url = 'https://selenium.dunossauro.live/aula_09_a'
b = Firefox()
b.get(url)
b.implicitly_wait(30)
# Espera IMPLÍCITA! Se o elemento não for encontrado em 30s, somente aí ele vai chamar a Exception
# Se ele conseguir achar antes disso, segue a vida!
# Ou seja, não significa que o programa vai sempre esperar 30s (pode ser menos)
elemento = b.find_element_by_css_selector('button')
elemento.click()
