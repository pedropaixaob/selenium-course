"""
Waits em janelas: new_window_is_opened e number_of_windows_to_be
"""

from selenium.webdriver import Firefox
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
new_window_is_opened,
number_of_windows_to_be
)

b = Firefox()
wdw = WebDriverWait(b, 60)

url = 'https://selenium.dunossauro.live/aula_11_b'
b.get(url)

b.find_element_by_id('popupd').click() # Pop-up com delay

wdw.until(new_window_is_opened(b.window_handles)) # Espero até que uma nova janela seja aberta
Print('Abriu!')

wdw.untiL(number_of_windows_to_be(2)) # Espero até que tenha 2 janelas
Print('Tem 2 janelas!')
