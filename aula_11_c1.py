"""
Manipular abas
"""

from selenium.webdriver import Firefox

b = Firefox()
url = 'https://selenium.dunossauro.live/aula_11_c'
b.get(url)

# execute_script permite que rodemos Window-APIs diretamente do código
b.execute_script('window.open("_blank")') # Passei _blank, mas poderia ser a url direto
b.switch_to.window(b.window_handles[-1]) # Trocar para última janela
b.get('http://ddg.gg')
