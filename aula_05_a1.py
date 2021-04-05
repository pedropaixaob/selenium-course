# atributos: globais, css, o DOM
# find: id, class, name
# elementos web: input, form

from selenium.webdriver import Firefox

firefox = Firefox()
url = 'http://selenium.dunossauro.live/aula_05_a.html'
firefox.get(url)

# div_1 = firefox.find_element_by_tag_name('div') daria o mesmo resultado
div_py = firefox.find_element_by_id('python')
div_hk = firefox.find_element_by_id('haskell')

print(div_py.find_element_by_tag_name('p').text)
print("")
print(div_hk.text)

firefox.quit()
