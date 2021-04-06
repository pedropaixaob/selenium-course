"""
Seletor universal: b.find_elements_by_css_selector('*')
(tentar evitar, em geral não são boas saídas)

Seletores combinados: podemos combinar seletores de forma sequencial
exs.
b.find_elements_by_css_selector('input[type$="t"]')  # tag input com atributo type iniciando por t
b.find_elements_by_css_selector('label[for*="n"]') # tag label com atributo for contendo a letra n

Seletores por lista:

# Encontra qualquer tag label juntamente a qualquer tag type
b.find_elements_by_css_selector('label','input')
# Encontra qualquer tag label que contenha o atributo for juntamente a quaisquer tags que tenham o atributo type com valor que termine em t
b.find_elements_by_css_selector('label[for]','*[type$="t"]')

OBS: não precisa ser os dois ao mesmo tempo ~ OU lógico.

"""
