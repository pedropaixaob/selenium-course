"""
Eventos que vamos estudar:

- Foco (focus)          aula 07
- Mudança (change)      aula 07
- Mouse                 aula 08
- Drag                  aula 08
- Teclado               aula 08

https://developer.mozilla.org/en-US/docs/Web/Events
"""


"""
FOCUS

Evento de foco. Quando o elemento é "acessado" ele está em foco. Com isso, o evento "Focus" é disparado.
Quando o elemento perde o foco, o evento Blur é disparado.

"""



"""
CHANGE

O evento de mudança [change] é desencadeado quando um elemento perde o foco [blur].
O elemento será analisado e, caso alguma mudança tenha ocorrido durante o período de foco, ele será disparado.

"""


from selenium.webdriver import Firefox
from time import sleep
b = Firefox()
url = 'https://selenium.dunossauro.live/aula_07_d'
b.get(url)


"""
1. Checar se a mudança ocorre no span (focus, blur)
2. Checar se a mudança ocorre no p (change)

"""

input_texto = b.find_element_by_tag_name('input')
span = b.find_element_by_tag_name('span')
p = b.find_element_by_tag_name('p')

"""
Quando clicar no elemento input, então o texto 'está com foco' deve ser o content de 'span'
Quando clicar no elemento span, então o texto 'está sem foco' deve ser o content de 'span'
"""
# input_texto.click()
# assert 'está com foco' == span.text     # Se eu quiser colocar para retornar uma msg no caso de erro, é só colocar no final , "mensagem"
# span.click()
# assert 'está sem foco' == span.text

"""
Dado que o texto '1' seja o content de 'p'
Quando enviar 'batata' no elemento 'input'
Então o texto 'está com foco' deve ser o content de 'span'
Quando clicar no elemento 'span'
Então o texto 'está sem foco' deve ser o content de 'span'
Então o texto '1' deve ser o content de 'p'
"""

sleep(5)
assert p.text == '0', 'p não é zero'
input_texto.send_keys('batata')
assert 'está com foco' == span.text, 'está com foco não está em span'
span.click()
assert 'está sem foco' == span.text, 'está sem foco não está em span'
assert p.text == '1', 'p não é um'
b.quit()
