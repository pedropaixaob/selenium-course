from selenium.webdriver import Firefox
from time import sleep

b = Firefox()
url = 'http://selenium.dunossauro.live/exercicio_06.html'
b.get(url)

conta_cliques = {'l0c0':0,'l0c1':0,'l1c0':0,'l1c1':0}

# Preencher um total de 5 formulários

for i in range(6):
    sleep(3)
    local = b.find_element_by_css_selector('span').text
    b.find_element_by_css_selector(f'.form-{local} input[name = "nome"]').send_keys('Pedro')
    b.find_element_by_css_selector(f'.form-{local} input[name = "senha"]').send_keys('senha123')
    b.find_element_by_css_selector(f'.form-{local} input[name = "{local}"]').click()


"""
Desafio: caso fossem 5 vezes de UM formulário específico

while all(cliques < 5 for cliques in conta_cliques.values()):
    sleep(3)
    local = b.find_element_by_css_selector('span').text
    b.find_element_by_css_selector(f'.form-{local} input[name = "nome"]').send_keys('Pedro')
    b.find_element_by_css_selector(f'.form-{local} input[name = "senha"]').send_keys('senha123')
    b.find_element_by_css_selector(f'.form-{local} input[name = "{local}"]').click()
    conta_cliques[f'{local}'] += 1
"""
