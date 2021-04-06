"""
Seletores são maneiras de encontrar elementos dentro de uma estrutura html (pode ser xml) que tem uma sintaxe própria e
nomenclaturas próprias. De maneira simplória é uma maneira de selecionar elementos usando os atributos dos próprios elementos.


 4 tipos de seletores:
- básicos: id, tipo (tag), classe, atributo, universal, combinados

  find_element_by_css_selector(...)
  - id: '#bla'
  - tag 'bla'
  - class: '.bla'

  obs: tb posso usar tag.classe (ex. b.find_elements_by_css_selector('div.form-group')

- seletores de grupo
- combinadores
- pseudo [classes, elementos]

"""

from selenium.webdriver import Firefox
from time import sleep

b = Firefox()
url = 'http://selenium.dunossauro.live/aula_06_a.html'
b.get(url)
b.find_element_by_css_selector('input').send_keys('Pedro')
