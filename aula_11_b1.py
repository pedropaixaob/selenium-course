"""
Janelas = Abas = Popups
Todos esses utilizam API de Window!
"""

from selenium.webdriver import Firefox
from time import sleep

b = Firefox()
url = 'https://selenium.dunossauro.live/aula_11_b'
b.get(url)

# b.current_window_handle #ID da janela atual
# wids = b.window_handles # lista dos IDS de todas as janelas

# Para mudar para uma janela específica, precisamos saber seu ID
# b.switch_to_window(b.window_handles[-1])

def find_window_url(url: str): # Encontra e move para a janela que contém uma string desejada no URL
    wids = b.window_handles
    for window in wids:
        b.switch_to.window(window)
        if url in b.current_url:
            break

def find_window_content(content: str): # Mudar para página que tem alguma string no código fonte da página
    wids = b.window_handles
    for window in wids:
        b.switch_to.window(window)
        if content in b.page_source:
            break

b.find_element_by_id('popup').click()
sleep(10)
find_window_content('<h1>popup')
