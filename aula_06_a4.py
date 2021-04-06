"""
Seletores combinadores

- Irmãos adjacentes
- Irmãos descendentes
- Grupos de irmãos
- Filhos
- Descendentes

- Irmãos adjacentes: pega  os elementos que estão no mesmo nível de identação do elemento dado (os primeiros, logo depois), com alguma condição

b.find_elements_by_css_selector('div + br')
Encontra qualquer br depois da div
OBS: Importante! Ele não pega o div, nesse caso. Ele vai pegar só os brs!
OBS2: Ele vai pegar apenas o primeiro br depois de cada div

Moral da história dos irmãos adjacentes: Parte de um elemento para encontrar outro!

- Geral adjacente: pega TODOS os elementos que estão no mesmo nível de identação do elemento dado

b.find_elements_by_css_selector(h2 ~ div)
Encontra TODAS as tags div que estão no mesmo nível de h2

- Filhos: a partir de alguém, pega os elementos que estão aninhados dentro dele, exatamente um nível depois
b.find_elements_by_css_selector(div > br)
Encontra todas as tags br que sejam filhas de div.

- Descendentes: pega todos os elementos que sejam filhos do elemento, direta ou indiretamente
b.find_elements_by_css_selector(form br)
Encontra todas as tags br que sejam filhas de form direta ou indiretamente

"""

from selenium.webdriver import Firefox
b = Firefox()
url = 'http://selenium.dunossauro.live/aula_06_a.html'
b.get(url)

# Pegar o (primeiro) irmão adjacente de div que é br
b.find_elements_by_css_selector('div + br')

# Irmãos adjacentes de (div class form-group) que são br
b.find_elements_by_css_selector('div.form-group + br')

# Da tag div com a classe form-group, pegue filhos são br
b.find_elements_by_css_selector('div.form-group > br')

# Da tag div com a classe form-group, pegue o filho com id dentro-nome
b.find_elements_by_css_selector('div.form-group > #dentro-nome') # filhos de um (div class form group) que tem id dentro-nome

b.find_elements_by_css_selector('h2 ~ div')

# Do formulário, pegue todas as tag label existentes, ignorando a hierarquia (descendente)
b.find_element_by_css_selector('form label')
