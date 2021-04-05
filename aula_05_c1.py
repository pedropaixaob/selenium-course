# atributos globais: id, class, autofocus, accesskey, title, hidden
# title é o que aparece quando colocamos o mouse em cima
# label
# input: formulário, botão...
# atributos específicos para o input: name, placeholder
# name: nome do formulário
# placeholder: o que vai aparecer enquanto nada for escrito

from selenium.webdriver import Firefox

firefox = Firefox()
url = 'http://selenium.dunossauro.live/aula_05_c.html'
firefox.get(url)

def melhor_filme(browser, filme, email, telefone):
    """ Preenche o formulário do melhor filme de 2020. """
    browser.find_element_by_name('filme').send_keys(filme)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('telefone').send_keys(telefone)
    browser.find_element_by_name('enviar').click()

melhor_filme (firefox, 'parasita', 'pedro@email.com', '(021)22222222')
