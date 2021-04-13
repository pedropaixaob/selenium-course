"""
Navegação - url_changes e url_to_be

class url_changes:
    def __init(self,url):
        self.url = url

    def __call__(self, driver):
        return self.url != driver.current_url

class url_to_be:
    def __init__(self, url):
        self.url = url

    def __call__(self, driver):
        return self.url == driver.current_url

# String está na URL?
class_url_contains(object):
    def __init__(self, url):
        self.url = url

    def __call__(self, driver):
        return self.url in driver.current_url


# Baseado em RegEx: Regex casa com a URL?
class url_matches(object):
    def __init__(self, pattern):
        self.pattern = pattern

    def __call__(self, driver):
        import re
        match = re.search(self.pattern, driver.current_url)

        return match is not None

# Título
class title_is:
    def __init__(self, title):
        self.title = title

    def __call__(self, driver):
        return self.title == driver.title

class title_contains:
    def __init__(self, title):
        self.title = title

    def __call__(self, driver):
        self.title in driver.title

"""

from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
url_changes, url_to_be, url_contains, url_matches, title_is, title_contains
)

url = 'https://selenium.dunossauro.live/aula_10_c.html'
b = Firefox()
b.get(url)

wdw = WebDriverWait(b, 10)

link = b.find_element_by_css_selector('.body_b a') # primeiro link(a) dentro do body b
link.click()

wdw.until(url_changes(url), 'URL não mudou') # Espera a modificação da URL acontecer

# wdw.until(url_to_be(url + "#")) # Aqui, eu envio a url que eu quero que seja depois da mudança
# wdw.until(url_contains('https'))
# wdw.until(url_matches('http(.*)live'))
# wdw.until(title_is('selenium'))
# wdw.until(title_contains('Aula 10b'))

print(url, b.current_url)
