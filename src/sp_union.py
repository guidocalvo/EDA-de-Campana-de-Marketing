#Tratamiento de datos
import pandas as pd

def union_archivos(df):
    """
    - Devuelve las dimensiones del DataFrame.
    - Muestra aleatoria de 5 filas del DataFrame.

    Parameters:
    df (pd.DataFrame): DataFrame a analizar.

    Returns:
    None
    
    """

    display(df.sample(5))

    print('-----------------')

    print('DIMENSIONES')

    print(f'Nuestro conjunto de datos presenta un total de {df.shape[0]} filas y {df.shape[1]} columnas')

