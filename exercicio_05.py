from selenium.webdriver import Firefox
from time import sleep

b = Firefox()
url = 'http://selenium.dunossauro.live/exercicio_05.html'
b.get(url)

sleep(5)
b.find_element_by_css_selector('.form-l0c0 input[name = "nome"]').send_keys('Pedro')
b.find_element_by_css_selector('.form-l0c0 input[name = "senha"]').send_keys('senha123')
b.find_element_by_css_selector('.form-l0c0 input[name = "l0c0"]').click()

b.find_element_by_css_selector('.form-l0c1 input[name = "nome"]').send_keys('Pedro')
b.find_element_by_css_selector('.form-l0c1 input[name = "senha"]').send_keys('senha123')
b.find_element_by_css_selector('.form-l0c1 input[name = "l0c1"]').click()

b.find_element_by_css_selector('.form-l1c0 input[name = "nome"]').send_keys('Pedro')
b.find_element_by_css_selector('.form-l1c0 input[name = "senha"]').send_keys('senha123')
b.find_element_by_css_selector('.form-l1c0 input[name = "l1c0"]').click()

b.find_element_by_css_selector('.form-l1c1 input[name = "nome"]').send_keys('Pedro')
b.find_element_by_css_selector('.form-l1c1 input[name = "senha"]').send_keys('senha123')
b.find_element_by_css_selector('.form-l1c1 input[name = "l1c1"]').click()
