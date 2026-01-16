#Tratamiento de datos
import pandas as pd
#--------------

#Visualización
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import KNNImputer, IterativeImputer


def subplot_col_cat(dataframe):

    """
    Genera gráfico subplot de columnas categóricas.

    Parameters:
    df (pd.DataFrame): DataFrame en el cual se procesarán las columnas categóricas.

    Returns:
    None
    """

     # Seleccionar columnas categóricas
    categorical_cols = dataframe.select_dtypes(include=['object', 'category']).columns

    cols_to_plot = [
        col for col in categorical_cols
        if dataframe[col].nunique() <= 200
    ]

    if len(categorical_cols) == 0:
        
        return "No hay columnas categóricas en el DataFrame."
    
    # Configurar el tamaño de la figura
    num_cols = len(categorical_cols)
    rows = (num_cols + 2) // 3  # Calcular filas necesarias para 3 columnas por fila
    fig, axes = plt.subplots(rows, 3, figsize=(15, rows * 5))
    axes = axes.flatten()  # Convertir los ejes a un array de una 1d plano para fácil iteración
    
    # Generar gráficos para cada columna categórica
    for i, col in enumerate(cols_to_plot):

        sns.countplot(data=dataframe, x=col, ax=axes[i], hue=col, palette="tab10", legend=False)
        axes[i].set_title(f'Distribution of {col}')
        axes[i].set_xlabel(col)
        axes[i].set_ylabel('Frecuency')
        axes[i].tick_params(axis='x', rotation=90)  # Rotar etiquetas si es necesario

    # Eliminar ejes sobrantes si hay menos columnas que subplots
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    # Ajustar diseño
    plt.tight_layout()
    plt.show()


def subplot_col_num (dataframe):

    """
    Genera gráfico subplot de columnas numéricas.

    Parameters:
    df (pd.DataFrame): DataFrame en el cual se procesarán las columnas categóricas.

    Returns:
    None
    """

    col_nums = dataframe.select_dtypes(include= 'number').columns
    num_graph = len(col_nums)

    num_rows = (num_graph +2 )//2


    fig, axes = plt.subplots(num_graph, 2, figsize=(15, num_rows*5))

    for i, col in enumerate(col_nums):

        sns.histplot(data=dataframe, x=col, ax=axes[i,0], bins=200)
        axes[i,0].set_title(f'Distribution of {col}')
        axes[i,0].set_xlabel(col)
        axes[i,0].set_ylabel('Frecuency')

        sns.boxplot(data=dataframe, x=col, ax = axes[i,1])
        axes[i,1].set_title(f'{col} boxplot')

    for j in range(i+1, len(axes)):
        fig.delaxes(axes[j])


    plt.tight_layout()
    plt.show()


def calculo_outliers (df, cols):

    """
    Devuelve valores outliers de un grupo de columnas seleccionado.

    Parameters:
    df (pd.DataFrame): DataFrame en el cual se procesarán las columnas categóricas.
    cols: Grupo de columnas.

    Returns:
    None
    
    """

    for col in cols:
        q_75 = df[col].quantile(0.75)
        q_25 = df[col].quantile(0.25)
        rango_itq = q_75-q_25
        inferior = q_25 - (rango_itq*1.5)
        superior = q_75 + (rango_itq*1.5)

        outliers = df[(df[col]< inferior) | (df[col] > superior)]
        num_outliers = len(outliers)

        per_outliers = num_outliers/df.shape[0]*100

        print(f"En la columna '{col}' tenemos {num_outliers} valores outliers, lo que representa un {per_outliers:.2f}% del total.")


def eliminar_outliers_iqr(df, cols):

    """
    Elimina valores outliers de un grupo de columnas seleccionado.

    Parameters:
    df (pd.DataFrame): DataFrame en el cual se procesarán las columnas categóricas.
    cols: Grupo de columnas.

    Returns:
    df_filtrado: Dataframe con valores filtrados.
    
    """

    #Se realiza sobre una copia del dataframe para no modificar el original.
    df_filtrado = df.copy()

    for col in cols:
        q_75 = df[col].quantile(0.75)
        q_25 = df[col].quantile(0.25)
        rango_itq = q_75-q_25
        inferior = q_25 - (rango_itq*1.5)
        superior = q_75 + (rango_itq*1.5)

        outliers = (df[col]< inferior) | (df[col] > superior)
        df_filtrado.loc[outliers, col] = pd.NA

    return df_filtrado



def imputar_iterative(dataframe, lista_columas):
    
    """
    Se aplica método estadístico iterative para completar valores nulos, 
    creará una nueva columna modificando los valores nulos por los resultados del método.

    Parameters:
    df (pd.DataFrame): DataFrame en el cual se procesarán las columnas categóricas.
    lista_columnas: lista de columnas a la que se le aplicara el método.

    Returns:
    dataframe: Se devuelve dataframe con la nueva columna.
    
    """
        
    iter_imputer = IterativeImputer(max_iter=50, 
                                random_state=42)
    data_imputed = iter_imputer.fit_transform(dataframe[lista_columas])
    new_col = [col + "_iterative" for col in lista_columas]
    dataframe[new_col] = data_imputed
    return dataframe


def imputar_knn(dataframe, lista_columas):

    """
    Se aplica método estadístico knn para completar valores nulos, 
    creará una nueva columna modificando los valores nulos por los resultados del método.

    Parameters:
    df (pd.DataFrame): DataFrame en el cual se procesarán las columnas categóricas.
    lista_columnas: lista de columnas a la que se le aplicara el método.

    Returns:
    dataframe: Se devuelve dataframe con la nueva columna.
    
    """

    knn_imputer = KNNImputer(n_neighbors=5)
    data_imputed = knn_imputer.fit_transform(dataframe[lista_columas])
    new_col = [col + "_knn" for col in lista_columas]
    dataframe[new_col] = data_imputed
    return dataframe