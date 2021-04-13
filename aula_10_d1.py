"""
Verificação de texto
Quero verificar se, dentro de um webelement, existe algum texto

text_to_be_present_in_element
text_to_be_present_in_element_value (por exemplo, nos forms, às vezes o texto que queremos buscar é o que está preenchendo o forms naquele momento)

# ATENÇÃO! OS DOIS RECEBEM LOCATORS, mesmo sem estar explicitado no nome

class text_to_be_present_in_element(object):
    def __init__(self, locator, text_):
        self.locator = locator
        self.text = text_

    def __call__(self, driver):
        try:
            element_text = find_element(driver, self.locator).text
            return self.text in element_text
        except StateElementReferenceException:
            False

class text_to_be_present_in_element_value(object):
    def __init__(self, locator, text_):
        self.locator = locator
        self.text = text_

    def __call__(self, driver):
        try:
            element_text = find_element(driver, self.locator).get_attribute("value")
            if element_text:
                return self.text in element_text
            else:
                return False
        except StateElementReferenceException:
            return False

"""

from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import (
text_to_be_present_in_element,
text_to_be_present_in_element_value)

url = 'https://selenium.dunossauro.live/aula_10_d.html'
b = Firefox()
b.get(url)

wdw = WebDriverWait(b, 50)

locator_h4 = (By.TAG_NAME, 'h4')
locator_nome = (By.CSS_SELECTOR, 'input[name="nome"]')

# Usando element
wdw.until(
text_to_be_present_in_element(locator_h4, 'Digite'))

# Preenche nome
b.find_element_by_css_selector(*locator_nome).send_keys('Pedro')

# Usando element_value
wdw.until(
text_to_be_present_in_element_value(
('css_selector', 'input[name="email"]'),
'disponível')

# Procura elemento e preenche formulário com e-mail
# (não usei locator dessa vez, só para mostrar que pode ser diferente)
b.find_element_by_css_selector(
*('css_selector', 'input[name="email])
).send_keys('pedro@pedromail.com')

print(url, b.current_url)
