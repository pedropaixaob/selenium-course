from selenium.webdriver import Firefox
from time import sleep

url = 'https://curso-python-selenium.netlify.app/aula_03.html'

# Poderia ser qualquer coisa ao invés de browser, tipo "navegador"
browser =  Firefox()
browser.get(url)

sleep(5)

a = browser.find_element_by_tag_name('a')

print(f'texto de a: {a.text}')

for click in range (10):
    # Atenção: se não colocarmos nada pro p, ele vai retornar apenas o primeiro!
    # p = browser.find_element_by_tag_name('p')

    ps = browser.find_elements_by_tag_name('p')
    a.click()
    print(f'Valor do último p: {ps[-1].text}, Valor do clique: {click}')

    # Atenção, os números da página vem como string!
    print(f'Os valores são iguais? {ps[-1].text == str(click)}')
browser.quit()
