from selenium.webdriver import Firefox
from time import sleep

url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'
browser = Firefox()
browser.get(url)
sleep(5)

ps = browser.find_elements_by_tag_name('p')
numero_esperado = ps[-1].text[-1]

a = browser.find_element_by_tag_name('a')

##### RESOLUÇÃO DO JOGO
resultado = 0
while numero_esperado != resultado:
    a.click()
    ps = browser.find_elements_by_tag_name('p')
    resultado = ps[-1].text[-1]
sleep(3)
browser.quit()
