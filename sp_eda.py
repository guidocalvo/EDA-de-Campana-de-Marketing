# Tratamiento de datos
import pandas as pd
#--------------

#Visualización
import matplotlib.pyplot as plt
import seaborn as sns



def eda_preliminar (df):

    """
    Realiza un análisis exploratorio preliminar sobre un DataFrame dado.

    Este análisis incluye:
    - Muestra aleatoria de 5 filas del DataFrame.
    - Información general del DataFrame (tipo de datos, nulos, etc.).
    - Porcentaje de valores nulos por columna.
    - Conteo de filas duplicadas.
    - Distribución de valores para columnas categóricas.

    Parameters:
    df (pd.DataFrame): DataFrame a analizar.

    Returns:
    None
    """


    display(df.sample(5))

    print('-----------------')

    print('DIMENSIONES')

    print(f'Nuestro conjunto de datos presenta un total de {df.shape[0]} filas y {df.shape[1]} columnas.')

    print('-----------------')

    print('INFO')

    display(df.info())  

    print('-----------------')
    print('NULOS')

    display(df.isnull().sum() / df.shape[0] * 100)

    print('-----------------')
    print('DUPLICADOS')

    print(f'Tenemos un total de {df.duplicated().sum()} duplicados.')

    print('-----------------')
    print('FRECUENCIA CATEGÓRICAS')
    
    for col in df.select_dtypes(include= 'object').columns:
        print(col.upper())
        print(df[col].value_counts())
        print('-------')

    print('-----------------')
    print('ESTADÍSTICOS NUMÉRICAS')
    display(df.describe().T)


def analisis_rapido(df, n=5):
        
    """
    Función que proporciona un análisis rápido del dataframe.

    Parameters:
    df (pd.DataFrame): DataFrame a analizar.
    n: número de filas (por defecto = 5)

    Returns:
    None
    """

    print(f"Las {n} primeras filas son:")
    display(df.head(n))
    print("Información básica del dataframe:")
    display(df.info())

    print(f"El número de duplicados es: {df.duplicated().sum()}")
    print("\nValores nulos: ")
    display(df.isnull().sum())


def eda(df, n=2):
    """
    Función que proporciona un eda rápido del dataframe.

    Parameters:
    df (pd.DataFrame): DataFrame a analizar.
    n: número de filas (por defecto = 5)

    Returns:
    None
    """

    num_cols = df.select_dtypes(include='number').columns
    cat_cols = df.select_dtypes(include=['object','category']).columns

    print("Variables numércias:\n\n", num_cols)
    print("\nVariables categóricas:\n\n", cat_cols)

    print("Veamos las estadísticas básicas:\n")
    display(df.describe().T.round(n))
    display(df.describe(include = ['category', 'object']).T.round(n))

    for col in cat_cols:
        print(f" \n ----------- ESTAMOS ANALIZANDO LA COLUMNA: '{col}' -----------\n")
        print(f"Valores únicos: {df[col].unique()}\n")
        print("Frecuencia de los valores únicos de las categorías:")
        display(df[col].value_counts())


def grafico_pastel(df,col):

    """
    Función que proporciona un gráfico tipo pastel.

    Parameters:
    df (pd.DataFrame): DataFrame a analizar.
    col: columna para graficar.

    Returns:
    None
    """

    col_counts = df[col].value_counts()

    # Gráfico de pastel
    plt.figure(figsize=(6, 6))
    plt.pie(
        col_counts,
        labels=col_counts.index,
        autopct='%1.1f%%',
        startangle=90,
        counterclock=False
    )
    plt.title(f'Distribution of {col}')
    plt.axis('equal')  # Para que sea un círculo
    plt.show()


def plot_categorical_vs_target(
    df,
    columns,
    target="y",
    cols=4,
    rotation=45,
    normalize=False
):
    
    """
    Dibuja gráficos de barras apiladas para variables categóricas
    mostrando la distribución del target (yes / no),
    ordenadas por frecuencia.

    Parameters:
    df (pd.DataFrame): DataFrame a analizar.
    columns: columnas para graficar.

    Returns:
    None
    """

    # Eliminar el target si está en columns
    columns = [col for col in columns if col != target]

    n = len(columns)
    rows = (n + cols - 1) // cols

    fig, axes = plt.subplots(
        rows, cols,
        figsize=(4 * cols, 4 * rows),
        squeeze=False
    )
    axes = axes.flatten()

    for i, col in enumerate(columns):
        ax = axes[i]

        # Ordenar categorías por frecuencia total
        order = df[col].value_counts().index

        grouped = (
            df
            .groupby([col, target])
            .size()
            .unstack(fill_value=0)
            .reindex(order)
        )

        if normalize:
            grouped = grouped.div(grouped.sum(axis=1), axis=0)

        grouped.plot(
            kind="bar",
            stacked=True,
            ax=ax
        )

        ax.set_title(f"{col} vs {target}")
        ax.set_xlabel(col)
        ax.set_ylabel("Proportion" if normalize else "Frecuency")
        ax.tick_params(axis="x", rotation=rotation)
        ax.legend(title=target)

    # Eliminar ejes sobrantes
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()


def campaign_acceptance(df, columns, target="y", positive="yes", cols=3):

    """
    Dibuja líneas de tasa de aceptación por columna,
    organizando 3 gráficos por fila.

    Parameters:
    df (pd.DataFrame): DataFrame a analizar.
    columns: columnas para graficar.

    Returns:
    None
    """

    n = len(columns)
    rows = (n + cols - 1) // cols  # filas necesarias

    fig, axes = plt.subplots(rows, cols, figsize=(5 * cols, 4 * rows), squeeze=False)
    axes = axes.flatten()

    for i, col in enumerate(columns):
        ax = axes[i]
        # Tasa de aceptación por 'columna'
        acceptance = df.groupby(col)[target].value_counts(normalize=True).unstack()
        ax.plot(acceptance.index, acceptance[positive], marker='o', color='seagreen', label='Acceptance')
        ax.set_title(f"Acceptance rate - {col}")
        ax.set_xlabel(col)
        ax.set_ylabel('Acceptance rate')
        ax.grid(True)
        ax.legend()

    # Ocultar ejes sobrantes
    for j in range(i + 1, len(axes)):
        axes[j].axis('off')

    plt.tight_layout()
    plt.show()





