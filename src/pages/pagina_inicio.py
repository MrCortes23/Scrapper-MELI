from selenium.webdriver.common.by import By
from .pagina_base import PaginaBase

#Abrir pagina principal y navegar a ofertas

class PaginaInicio(PaginaBase):
    URL_PRINCIPAL = 'https://www.mercadolibre.com.co'
    BOTON_OFERTAS = (
        By.XPATH,
        "//a[contains(normalize-space(.), 'Ofertas') or contains(normalize-space(.), 'OFERTAS')]")

    def cargar_pagina(self) -> None:
        self.driver.get(self.URL_PRINCIPAL)

    def ir_a_ofertas(self) -> None:
        self.hacer_clic(self.BOTON_OFERTAS)