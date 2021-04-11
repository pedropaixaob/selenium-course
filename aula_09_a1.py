"""
Waits

Dois tipos de espera: explícitos e implícitos
Aqui trataremos de implícitos, explícitos apenas no próximo arquivo
- Implícitas: espera todos os eventos, navegação, com um tempo padrão
browser.implicitly_wait(30)

PRÓS:

- Funciona em cenários Flaky
- Espera até acontecer algo

CONTRAS:
- Segura a aplicação por mais tempo
- Tudo é esperado tendo o mesmo tempo como base (não temos como estabelecer prioridade de carregamento)
- Não funciona para elementos específicos
- Se algo der errado, vai demorar o tempo do wait para saber
"""

from selenium.webdriver import Firefox
url = 'https://selenium.dunossauro.live/aula_09_a'
b = Firefox()
b.get(url)
b.implicitly_wait(30)

# Espera IMPLÍCITA! Se o elemento não for encontrado em 30s, somente aí ele vai chamar a Exception
# Se ele conseguir achar antes disso, segue a vida!
# Ou seja, não significa que o programa vai sempre esperar 30s (pode ser menos)
btn = b.find_element_by_css_selector('button')
btn.click()

sucesso = b.find_element_by_css_selector('#finished') # id finished
assert sucesso.text == 'Carregamento concluído'
