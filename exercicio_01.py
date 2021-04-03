from selenium.webdriver import Firefox
from time import sleep

url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'
browser = Firefox()
browser.get(url)
sleep(5)

h1 = browser.find_element_by_tag_name('h1')
ps = browser.find_elements_by_tag_name('p')


dic = {h1.text:
    {
    ps[0].get_attribute('atributo'): ps[0].text,
    ps[1].get_attribute('atributo'): ps[1].text,
    ps[2].get_attribute('atributo'): ps[2].text
    }
    }

browser.quit()

print(dic)
