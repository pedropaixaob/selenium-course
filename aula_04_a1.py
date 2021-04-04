url = 'http://selenium.dunossauro.live/aula_04_a.html'

from selenium.webdriver import Firefox

browser = Firefox()
browser.get(url)

lista_nao_ordenada = browser.find_element_by_tag_name('ul')
lis = lista_nao_ordenada.find_elements_by_tag_name('li')

# Se eu não uso um outro find_element_by_tag_name, no caso de uma estrutura aninhada,
# text vai ler tudo de text que tem na tag, mesmo que estejam web elements distintos

lis[0].find_element_by_tag_name('a').text

""""
1. Buscamos `ul` (primeiro)
2. Buscamos todos `li` dentro do ul
3. No primeiro `li`, buscamos `a`

ul
    li
        a
            texto
    li
        a
            texto
""""
