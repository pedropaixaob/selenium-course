"""
Abordagem similar, utilizando OO
Evitar uso do partial: '__call__'
Abordagem tradicional, não necessariamente a melhor (depende do contexto)
"""

"""

class EsperarElemento:
    def __init__(self, by, selector):
        self.locator = (by, selector)

    def __call__(self, driver):
        if web_drive.find_elements(*locator):
            return True
        return False

wdw.until(EsperarElemento(By.ID, 'meu_id')
"""
