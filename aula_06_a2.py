"""
Vários tipos de maneiras de pegar atributos
https://developer-mozilla.org/en-US/docs/Web/CSS/Attribute_selectors

Dois tipos de atributos:
[atributo]
[atributo operador valor]
obs: existe uma terceira (nova) sintaxe, mas ainda não está sendo utilizada em todos os browsers

b.find_elements_by_css_selector('[bla]') # não especifico o valor do atributo, só qual é o atributo

exs.
b.find_elements_by_css_selector('[for]')
b.find_elements_by_css_selector('[type]')
b.find_elements_by_css_selector('[name]')

[atributo=valor]          deve ser exatamente igual
[atributo*=valor]         deve ocorrer em
[atributo|=valor]         deve ser exatamente ou iniciar (não olha caracteres isoladamente, só espaço)
[atributo^=valor]         iniciado em
[atributo$=valor]         terminado em
[atributo~=valor]         um deve ser exatamente igual

"""

from selenium.webdriver import Firefox
from time import sleep

b = Firefox()
url = 'http://selenium.dunossauro.live/aula_06_a.html'
b.get(url)

# b.find_elements_by_css_selector('[class="form-group"]') # só o que for EXATAMENTE form-group. Não pega se tiver algo a mais!
# b.find_elements_by_css_selector('[class*="group"]') # todas as classes que tenham, em algum momento, a palavra group
# b.find_elements_by_css_selector('[type$="t"]') # todos os types que terminam em t

""" Usando o atributo 'type' [attr=valor]
nome = b.find_element_by_css_selector('[type="text"]')
senha = b.find_element_by_css_selector('[type="password"]')
btn = b.find_element_by_css_selector('[type="submit"]')
"""

""" Usando o atributo 'name' [attr=valor]
nome = b.find_element_by_css_selector('[name="nome"]')
senha = b.find_element_by_css_selector('[name="senha"]')
btn = b.find_element_by_css_selector('[name="l0c0"]')
"""

""" Usando o atributo 'name' [attr*=valor]
nome = b.find_element_by_css_selector('[name*="ome"]')
senha = b.find_element_by_css_selector('[name*="nha"]')
btn = b.find_element_by_css_selector('[name*="l0"]')
"""

""" Usando o atributo 'name' [attr|=valor]
nome = b.find_element_by_css_selector('[name|="nome"]')
senha = b.find_element_by_css_selector('[name|="senha"]')
btn = b.find_element_by_css_selector('[name|="l0c0"]')
"""

""" Usando o atributo 'name' [attr^=valor] """
nome = b.find_element_by_css_selector('[name^="n"]')
senha = b.find_element_by_css_selector('[name^="s"]')
btn = b.find_element_by_css_selector('[name^="l"]')

nome.send_keys('Pedro')
senha.send_keys('senha123')
# btn.click()

# https://selenium.dunossauro.live/aula_06_a.html?nome=Pedro&senha=senha123&l0c0=Enviar%21#
