# 📊 Análisis EDA – Campaña de Marketing Bancario


## 📖 Descripción del Proyecto

Este proyecto realiza un Análisis Exploratorio de Datos (EDA) correspondiente a campañas de marketing directo realizadas por una institución bancaria portuguesa.

Las campañas se llevaron a cabo principalmente mediante llamadas telefónicas, y en muchos casos fue necesario contactar al mismo cliente más de una vez para determinar si el producto ofrecido (un depósito a plazo) sería finalmente suscrito.

El objetivo principal del análisis es identificar los factores que influyen en la decisión del cliente y obtener conclusiones relevantes a partir de los datos.


## 📂 Descripción de los Datos

### Dataset 1: `bank-additional.csv`

Contiene información relacionada con las campañas de marketing y variables macroeconómicas.

**Columnas principales:**

- `age`: Edad del cliente.
- `job`: Ocupación o profesión.
- `marital`: Estado civil.
- `education`: Nivel educativo.
- `default`: Historial de incumplimiento de pagos (1: Sí, 0: No).
- `housing`: Préstamo hipotecario (1: Sí, 0: No).
- `loan`: Préstamo personal (1: Sí, 0: No).
- `contact`: Método de contacto utilizado.
- `duration`: Duración de la última llamada (en segundos).
- `campaign`: Número de contactos durante la campaña actual.
- `pdays`: Días desde el último contacto previo.
- `previous`: Número de contactos previos a esta campaña.
- `poutcome`: Resultado de la campaña anterior.
- `emp.var.rate`: Tasa de variación del empleo.
- `cons.price.idx`: Índice de precios al consumidor.
- `cons.conf.idx`: Índice de confianza del consumidor.
- `euribor3m`: Tasa de interés Euribor a 3 meses.
- `nr.employed`: Número de empleados.
- `y`: Variable objetivo (suscripción: Sí / No).
- `date`: Fecha de contacto.
- `contact_month`: Mes del contacto.
- `contact_year`: Año del contacto.
- `id_`: Identificador único del cliente.


### Dataset 2: `customer-details.xlsx`

Archivo Excel con información demográfica y de comportamiento de clientes.  
Contiene tres hojas, correspondientes a diferentes años, que fueron unificadas en un solo DataFrame.

**Columnas:**

- `Income`: Ingreso anual del cliente.
- `Kidhome`: Número de niños en el hogar.
- `Teenhome`: Número de adolescentes en el hogar.
- `Dt_Customer`: Fecha de alta del cliente.
- `NumWebVisitsMonth`: Visitas mensuales al sitio web.
- `ID`: Identificador único del cliente


## ✅ Requisitos del proyecto

A lo largo del proyecto tienes que cubrir los siguientes puntos:

- Transformación y limpieza de los datos.
- Análisis descriptivo de los datos.
- Visualización de los datos.
- Informe explicativo del análisis.


## 🗂️ Estructura del Proyecto


├── data/          # Archivos de datos originales y procesados

├── notebooks/     # Jupyter Notebooks del análisis

├── src/           # Funciones auxiliares

└── README.md      # Descripción del proyecto


## 📥 Primera lectura de los datos y unión en un archivo común

Para comenzar, importamos el data_raw.csv, presentamos unas filas de ejemplo y vemos que contiene 43.000 filas y 28 columnas.
Luego, importamos el archivo customer-details.xlsx y unimos todas las hojas en un solo dataframe.
Unimos ambos dataframe a través de la columna en común que es el ID del cliente. Para esto utilizamos el método merge, borramos los índices y la columna sobrante ID.


## 🔍 EDA preliminar

Aquí, ejecutamos una función que nos permite hacer un análisis exploratorio preliminar del dataframe.
Este análisis incluye:

- Muestra aleatoria de 5 filas del DataFrame.

- Información general del DataFrame (tipo de datos, nulos, etc.).

- Porcentaje de valores nulos por columna.

- Conteo de filas duplicadas.

- Distribución de valores para columnas categóricas.

A partir de este informe, definimos la estrategia que necesitamos para realizar la limpieza y transformación de los datos.


## 🧹 Limpieza de los Datos

- Cambio de nombres de columnas y valores a minúsculas.

- Transformación de fechas (dt_customer, date) a formato date.

- Crear columna de binario a str. Se utiliza para default, housing y loan.

- Cambio de , por . y conversión a float.

- Creación de columnas contact_month y contact_year que aparecian en el enunciado.

- Exportación del dataset limpio.


## 🚫 Tratamiento de nulos


### Nulos categóricos

Se reemplazan por una nueva categoría, como "Desconocido", cuando haya una gran cantidad de nulos o cuando no haya ninguna categoría que destaque frente al resto.

job - tiene 345 valores nulos (0,8%).

education - tiene 1807 valores nulos (4,2%).

housing y housing_str - tiene 1026 valores nulos (2,38%).

date, contact_year y contact_month - tiene 248 valores nulos (0,57%).

Los valores nulos de las columnas job, education, date, contact_month, contact_year, housing y housing_str, serán reemplazados por la una nueva categoría llamada unknown ya que ninguna de sus respectivas categorías destaca sobre el resto.

Los valores nulos de las columnas marital, default, default_str, loan y loan_str, serán reemplazados por su respectiva moda ya que se destacan sobre el resto de los valores. ··


### Outliers numéricos

campaign - tiene 2504 valores outliers (5,82%).

duration - tiene 3072 valores outliers (7,14%).

age - tiene 441 valores outliers (1,03%).

cons.conf.idx - tiene 477 valores outliers (1,11%).

Borramos los outliers de age y cons.conf.idx ya que representan menos del 5% de los datos. ··


### Nulos numéricos

age – tiene 997 valores nulos (12,93%).

cons.price.idx – tiene 471 valores nulos (1.10%).

cons.conf.idx – tiene 477 valores nulos (1.11%).

euribor3m – tiene 9256 valores nulos (21.53%).


Como cons.price.idx y cons.conf.idx tienen un porcentaje de nulos muy pequeño vamos a eliminarlos y rellenamos los valores de nulos de age con la mediana.

Solo nos queda con nulos la columna euribor3m, como tiene un porcentaje muy alto de nulos, crearemos una nueva columna tipo flag que indicará el dato faltante y los nulos originales los completamos a través de los métodos estadísticos iterative y knn.

Los métodos euribor3m_iterative y euribor3m_knn arrojan el mismo resultado así que, eliminamos uno de los dos y la columna original de euribor3m.


## 📊 Análisis Exploratorio de Datos (EDA)

En esta sección se analizan las principales variables de la base de datos Bank Marketing, con el objetivo de identificar qué factores influyen en la decisión del cliente de suscribirse a un depósito a plazo. El análisis se centra tanto en variables demográficas como en variables relacionadas con la campaña de marketing y el contexto económico.


## 📝 Conclusiones

A partir del análisis exploratorio realizado, se pueden extraer las siguientes conclusiones principales:

- La variable objetivo se encuentra fuertemente desbalanceada, ya que la gran mayoría de los clientes no se han suscrito al producto ofrecido. Esto es un aspecto relevante a considerar en etapas posteriores de modelado.

- La edad del cliente muestra una influencia clara en la decisión de suscripción. Se observan tasas de aceptación más elevadas en personas menores de 30 años y mayores de 60, destacándose especialmente los estudiantes y jubilados como los grupos con mayor probabilidad de suscripción.

- Las variables demográficas tradicionales como estado civil, nivel de ingresos, número de hijos o cantidad de visitas a la web no presentan diferencias significativas en las tasas de aceptación.

- En relación con la frecuencia de contacto, se observa que el mayor porcentaje de éxito ocurre cuando el cliente es contactado entre una y dos veces, lo que sugiere que los clientes interesados tienden a aceptar la propuesta rápidamente. Asimismo, el número de contactos realizados en campañas previas parece influir, ya que las mayores tasas de suscripción se concentran entre dos y seis contactos anteriores.

- El tipo de contacto también resulta relevante: las llamadas realizadas a teléfonos móviles presentan una mayor tasa de suscripción en comparación con las realizadas a teléfonos fijos.

- Por último, las variables relacionadas con el contexto económico, como la variación en la tasa de empleo y los indicadores de precios al consumidor, no muestran una relación clara con la decisión de suscripción, lo que indica que su impacto en este conjunto de datos es reducido.

- En conjunto, el análisis sugiere que las variables asociadas a la estrategia de contacto y al perfil etario del cliente tienen un mayor impacto en la aceptación del producto, mientras que los factores demográficos y macroeconómicos presentan una influencia limitada.


## 🤝 Contribuciones

Las contribuciones son bienvenidas. Puedes sugerir nuevas consultas, correcciones o mejoras estructurales.


## ✍️ Autores

Guido Julián Calvo Sio
