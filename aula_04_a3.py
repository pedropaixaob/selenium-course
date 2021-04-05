from selenium.webdriver import Firefox
from urllib.parse import urlparse

browser = Firefox()
url = 'http://selenium.dunossauro.live/aula_04_a.html'
browser.get(url)

# browser.refresh()
# browser.title()

url_parseado = urlparse(browser.current_url)

# url_parseado.scheme
# url_parseado.netloc
# url_parseado.path
