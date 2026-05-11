from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from typing import Any, Tuple
import time

#Acciones comunes para las paginas

class PaginaBase:
    def __init__(self, driver: Any, tiempo_espera: int = 10) -> None:
        self.driver = driver
        self.tiempo_espera = tiempo_espera
        self.wait = WebDriverWait(driver, tiempo_espera)

    def encontrar_elemento(self, locator: Tuple[str, str]) -> Any:
        """Encuentra un elemento con wait explícito y manejo de elementos stale."""
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException as error:
            raise TimeoutException(
                f"No se encontró el elemento con locator {locator}: {error}"
            ) from error

    def hacer_clic(self, locator: Tuple[str, str], reintentos: int = 3) -> None:
        """Hace clic en un elemento con reintentos en caso de StaleElementReferenceException."""
        for intento in range(reintentos):
            try:
                elemento = self.wait.until(EC.element_to_be_clickable(locator))
                elemento.click()
                return
            except StaleElementReferenceException:
                if intento < reintentos - 1:
                    time.sleep(0.5)
                    continue
                raise TimeoutException(
                    f"No se pudo hacer clic (elemento stale) en {locator} tras {reintentos} reintentos"
                )
            except TimeoutException as error:
                raise TimeoutException(
                    f"No se pudo hacer clic en el elemento con locator {locator}: {error}"
                ) from error

