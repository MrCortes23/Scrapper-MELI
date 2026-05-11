# Scraper de Ofertas - Mercado Libre Colombia

Script de automatización en Python con Selenium para extraer datos de productos en la sección de ofertas de Mercado Libre Colombia. Los datos se guardan en un archivo Excel.

---

## Requisitos previos

- Python 3.10 o superior
- Google Chrome o Microsoft Edge instalado
- Conexión a internet

No es necesario descargar ChromeDriver manualmente, el script lo gestiona solo con `webdriver-manager`.

---

## Instalación

**1. Clonar o descargar el proyecto**

```bash
git clone <url-del-repositorio>
cd Prueba_Tecnica_MELI
```

**2. Crear entorno virtual (recomendado)**

```bash
python -m venv env
```

Activar el entorno:

- Windows:
  ```bash
  env\Scripts\activate
  ```
- Linux / macOS:
  ```bash
  source env/bin/activate
  ```

**3. Instalar dependencias**

```bash
pip install -r requirements.txt
```

---

## Cómo ejecutar

Con Chrome (por defecto):

```bash
python main.py
```

Con Edge:

```bash
# Windows
set NAVEGADOR=edge && python main.py

# Linux / macOS
export NAVEGADOR=edge && python main.py
```

El archivo de resultados se genera en `data_excel/productos_ofertas.xlsx`.

---

## Estructura del proyecto

```
Prueba_Tecnica_MELI/
│
├── main.py                     # Archivo principal, orquesta todo el flujo
├── requirements.txt            # Dependencias
├── README.md
│
├── data_excel/
│   └── productos_ofertas.xlsx  # Archivo generado con los datos
│
└── src/
    ├── data_export.py          # Exporta los datos a Excel usando pandas
    └── pages/
        ├── pagina_base.py      # Clase base con los waits y métodos comunes
        ├── pagina_inicio.py    # Abre la página principal y navega a ofertas
        └── pagina_ofertas.py   # Extrae los datos de los productos
```

---

## Datos que se extraen

De cada producto se obtiene:

| Campo | Descripción | Disponibilidad |
|---|---|---|
| `nombre` | Nombre del producto | Siempre |
| `precio_actual` | Precio con descuento | Siempre |
| `precio_anterior` | Precio original | Solo si aplica |
| `descuento` | Porcentaje de descuento | Solo si aplica |
| `link` | URL del producto | Siempre |
| `vendedor` | Nombre del vendedor | Cuando está disponible |
| `calificacion` | Puntuación y reseñas | Cuando está disponible |
| `cuotas` | Información de cuotas | Cuando está disponible |
| `envio_gratis` | Si tiene envío gratis | Cuando está disponible |

---

## Detalles técnicos

El proyecto usa el patrón Page Object Model (POM), donde cada página del sitio tiene su propia clase. La clase `PaginaBase` centraliza los métodos de interacción con elementos usando waits explícitos de Selenium (`WebDriverWait` y `expected_conditions`).

Para los clics se implementaron reintentos automáticos para manejar el `StaleElementReferenceException`, que es común en páginas con contenido dinámico.

El timeout por defecto es de 10 segundos y la cantidad de productos a extraer es 10, ambos modificables en el código.

---

