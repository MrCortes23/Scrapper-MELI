import pandas as pd

#crear el xslx (excel) con los datos obtenidos

def exportar_datos(datos, ruta):
    df = pd.DataFrame(datos)
    df.to_excel(ruta, index=False)