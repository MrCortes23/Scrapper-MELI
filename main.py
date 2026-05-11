import traceback
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from src.pages.pagina_inicio import PaginaInicio
from src.pages.pagina_ofertas import PaginaOfertas
from src.data_export import exportar_datos

#Inicializacion del driver, navegacion, extraccion de datos y exportacion a excel, 
#usando clases para cada pagina y funciones para cada accion. Manejo de errores 
#y optimizacion del driver.

def crear_driver(navegador: str = "chrome"):
    """Crea instancia del navegador con opciones optimizadas."""
    opciones_comunes = [
        "--start-maximized",
        "--disable-blink-features=AutomationControlled",
        "--disable-gpu",
        "--no-sandbox",
        "--disable-dev-shm-usage",
    ]
    
    if navegador.lower() == "chrome":
        try:
            opciones = webdriver.ChromeOptions()
            for arg in opciones_comunes:
                opciones.add_argument(arg)
            opciones.add_experimental_option("excludeSwitches", ["enable-automation"])
            opciones.add_experimental_option("useAutomationExtension", False)
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=opciones)
            print("Navegador Chrome inicializado")
            return driver
        except Exception as e:
            print(f"Error al inicializar Chrome: {e}")
            raise
    elif navegador.lower() == "edge":
        try:
            opciones = webdriver.EdgeOptions()
            for arg in opciones_comunes:
                opciones.add_argument(arg)
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=opciones)
            print("Navegador Edge inicializado")
            return driver
        except Exception as e:
            print(f"Error al inicializar Edge: {e}")
            print("Nota: Asegúrate de tener Edge instalado en tu sistema.")
            raise
    else:
        raise ValueError(f"Navegador no soportado: {navegador}. Usa 'chrome' o 'edge'")


def main(navegador: str = "chrome"):
    driver = crear_driver(navegador)

    try:
        print("Iniciando navegador...")
        pagina_inicio = PaginaInicio(driver)
        pagina_inicio.cargar_pagina()
        print("Cargando página principal...")
        pagina_inicio.ir_a_ofertas()
        print("Navegando a ofertas...")

        pagina_ofertas = PaginaOfertas(driver)
        datos = pagina_ofertas.obtener_datos_productos(10) #Número de productos a extraer
        print(f"Extrayendo datos de {len(datos)} productos...")

        exportar_datos(datos, 'data_excel/productos_ofertas.xlsx')
        print("Datos exportados a Excel.")

    except Exception:
        print("Error durante la ejecución:")
        print(traceback.format_exc())
    finally:
        driver.quit()
        print("Navegador cerrado.")


if __name__ == "__main__":
    # Se puede cambiar el navegador: el predeterminado es 'chrome'
    # Usar: set NAVEGADOR=edge && python main.py en el cmd para usar Edge
    navegador = os.getenv('NAVEGADOR', 'chrome').strip()
    main(navegador)