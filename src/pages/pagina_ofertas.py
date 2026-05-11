from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .pagina_base import PaginaBase
from typing import List, Dict, Any

#extraccion de pagina ofertas y datos de productos

class PaginaOfertas(PaginaBase):
    TARJETA_PRODUCTO = (By.CSS_SELECTOR, "div.poly-card__content")
    NOMBRE = (By.CSS_SELECTOR, "a.poly-component__title")
    PRECIO_ACTUAL = (By.CSS_SELECTOR, "div.poly-price__current span.andes-money-amount__fraction")
    PRECIO_ANTERIOR = (By.CSS_SELECTOR, "s.andes-money-amount--previous span.andes-money-amount__fraction")
    DESCUENTO = (By.CSS_SELECTOR, "span.andes-money-amount__discount")
    LINK = (By.CSS_SELECTOR, "a.poly-component__title")
    VENDEDOR = (By.CSS_SELECTOR, "span.poly-component__seller")
    CALIFICACION = (By.CSS_SELECTOR, "span.poly-reviews__rating")
    CALIFICACION_TOTAL = (By.CSS_SELECTOR, "span.poly-reviews__total")
    CUOTAS = (By.CSS_SELECTOR, "span.poly-price__installments")
    ENVIO_GRATIS = (By.XPATH, ".//span[contains(text(), 'Envío gratis')]")


    def obtener_datos_productos(self, cantidad: int = 5) -> List[Dict[str, Any]]:
        self.wait.until(EC.presence_of_all_elements_located(self.TARJETA_PRODUCTO))
        tarjetas = self.driver.find_elements(*self.TARJETA_PRODUCTO)
        productos = []
        for tarjeta in tarjetas[:cantidad]:
            nombre = tarjeta.find_element(*self.NOMBRE).text
            precio_actual = tarjeta.find_element(*self.PRECIO_ACTUAL).text
            try:
                precio_anterior = tarjeta.find_element(*self.PRECIO_ANTERIOR).text
            except Exception:
                precio_anterior = 'N/A'
            try:
                descuento = tarjeta.find_element(*self.DESCUENTO).text
            except Exception:
                descuento = 'N/A'
            try:
                vendedor = tarjeta.find_element(*self.VENDEDOR).text
            except Exception:
                vendedor = 'N/A'
            # Extraer calificación: nota y total de reseñas si están disponibles
            try:
                nota = tarjeta.find_element(*self.CALIFICACION).text
            except Exception:
                nota = None
            try:
                total = tarjeta.find_element(*self.CALIFICACION_TOTAL).text
            except Exception:
                total = None
            if nota and total:
                calificacion = f"{nota} {total}"
            elif nota:
                calificacion = nota
            elif total:
                calificacion = total
            else:
                calificacion = 'N/A'
            try:
                cuotas = tarjeta.find_element(*self.CUOTAS).text
            except Exception:
                cuotas = 'N/A'
            try:
                envio_gratis = tarjeta.find_element(*self.ENVIO_GRATIS).text
            except Exception:
                envio_gratis = 'N/A'
            link = tarjeta.find_element(*self.LINK).get_attribute('href')
            productos.append({
                'nombre': nombre,
                'precio_actual': precio_actual,
                'precio_anterior': precio_anterior,
                'descuento': descuento,
                'vendedor': vendedor,
                'calificacion': calificacion,
                'cuotas': cuotas,
                'envio_gratis': envio_gratis,
                'link': link
            })
        return productos