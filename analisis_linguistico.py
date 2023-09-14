# Análisis de una Noticia en Internet

# En este análisis, se trabaja con una noticia obtenida de una página web. Se extrae el contenido HTML y se filtra para llevar a cabo un análisis lingüístico. La noticia seleccionada lleva el título "Lluvias del fin de semana provocaron afectaciones en Golfito, Esparza, Quepos y Garabito" y se almacena en la variable `text`.

# Descripción del Análisis:

# El objetivo de este análisis es utilizar herramientas de procesamiento de lenguaje natural (NLP) y expresiones regulares para comprender mejor el contenido de la noticia. A continuación, se detallan los pasos clave del proceso:

# 1. **Extracción de HTML**: Se obtiene el contenido completo de la página web, incluyendo el formato HTML.

# 2. **Filtrado de Contenido**: Se realiza un filtrado para extraer únicamente el texto relevante de la noticia, eliminando etiquetas y elementos HTML innecesarios.

# 3. **Identificación de Oraciones**: Se utilizan expresiones regulares para identificar y extraer las oraciones clave de la noticia.

# 4. **Identificación de Tokens**: Se definen tokens como las palabras dentro de las oraciones. Estos tokens se extraen mediante el uso de expresiones regulares.

# 5. **Análisis de Frecuencia**: Se analiza la frecuencia de cada término en el vocabulario para comprender mejor los temas clave de la noticia.

# Noticia Seleccionada

# La noticia seleccionada para este análisis lleva el siguiente título:

# **"Lluvias del fin de semana provocaron afectaciones en Golfito, Esparza, Quepos y Garabito"**

# Esta noticia es fundamental para llevar a cabo el análisis lingüístico y explorar su contenido en detalle.

# Código Fuente

# A continuación, se muestra el código utilizado para realizar el análisis:

import requests
from bs4 import BeautifulSoup

# copiamos el url de la noticia, puede ser cualquier noticia
url = "https://delfino.cr/2023/09/lluvias-del-fin-de-semana-provocaron-afectaciones-en-golfito-esparza-quepos-y-garabito"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

# se guardo el codigo html en una variable text
text = soup.find("html")

# se imprime la variable text para ver el codigo en html
print(text)

"""## Separamos las oraciones del codigo HTML usando expresiones regulares"""

# importamos la biblioteca de expresiones regulares
import re

# copiamos el texto a una variable string
input_string = str(text)

# filtramos cada uno de los tokens dentro de las <> para que solo queden las oraciones
# NOTA: no podia ser solo r'<[^<>]+>' como se tenia al inicio ya que contaba el codigo
# en javascript que no se ocupaba
output_string = re.sub(r'<script.*?>.*?</script>', ' ', input_string, flags=re.DOTALL)
output_string = re.sub(r'<style .*?>.*?</style>', ' ', output_string, flags=re.DOTALL)
output_string = re.sub(r'<[^<>]+>', ' ', output_string)

# se imprime el string con solo las oraciones de la noticia del html original
print(output_string)

"""## Para seperarlos por oraciones usamos la expresion regular: r'.*.'"""

expresion = r'.*.'
tokens = re.findall(expresion, output_string)
print(tokens)
print('Cantidad de oraciones: ', len(tokens))

"""## Para separarlos por palabras usamos la expresion regular: r'\w+'

"""

expresion = r'\w+'
tokens = re.findall(expresion, output_string)
print(tokens)
print('Cantidad de palabras: ', len(tokens))

"""## Para contar las palabras diferentes y su frecuencia

"""

def contar_palabras_distintas(tokens):
  palabra = set(tokens)
  frecuencia = {}
  for value in palabra:
    frecuencia[value] = tokens.count(value)

  return frecuencia
palabras_contador = contar_palabras_distintas(tokens)
print(palabras_contador)

"""## Se grafica la frecuencia de las palabras usando un grafico de barras"""

import matplotlib.pyplot as plt
import numpy as np

# obtenemos la lista de palabras
palabras = list(palabras_contador.keys())

# obtenemos la cantidad que se usa la palabra
cantidad = list(palabras_contador.values())

# valores para el eje x
x = np.arange(len(palabras))

# crea una grafica de barras
plt.bar(x, cantidad, color="green")

# nombramos los ejes en x y en y
plt.xlabel("Palabras")
plt.ylabel("Cantidad de veces usada")

# titulo de la grafica
plt.title("Histograma de la frecuencia de palabras en una noticia")

# mostrar el grafico
plt.show()

"""## Para ver las palabras mas usadas de manera ordenada de mayor uso a menor uso"""

# ordenamos de mayor a menor
sorted_palabras_contador = dict(sorted(palabras_contador.items(), key=lambda item: item[1], reverse=True))

# obtenemos las palabras con mayor frecuencia y las frecuencias de las respectivas palabras
top_palabras = list(sorted_palabras_contador.keys())[:]
top_frequencias = [sorted_palabras_contador[word] for word in top_palabras]

# se define el eje x
x = np.arange(len(top_palabras))
print(len(x))
# se crea la grafica de barras
plt.bar(x, top_frequencias, color="green")

# rotamos las palabras para que se puedan leer mejor
plt.xticks(x, top_palabras, rotation=45)

# se titula la grafica y los ejes
plt.xlabel("Palabras")
plt.ylabel("Cantidad de veces usada")
plt.title("Palabras más frecuentes en una noticia")

# para mostrar la grafica
plt.show()

"""## Para ver el top 10 de las palabras mas usadas en una noticia"""

# ordenamos de mayor a menor
sorted_palabras_contador = dict(sorted(palabras_contador.items(), key=lambda item: item[1], reverse=True))

# obtenemos las palabras con mayor frecuencia y las frecuencias de las respectivas palabras
top_palabras = list(sorted_palabras_contador.keys())[:10]
top_frequencias = [sorted_palabras_contador[word] for word in top_palabras]

# se define el eje x
x = np.arange(len(top_palabras))

# se crea la grafica de barras
plt.bar(x, top_frequencias, color="green")

# rotamos las palabras para que se puedan leer mejor
plt.xticks(x, top_palabras, rotation=45)

# se titula la grafica y los ejes
plt.xlabel("Palabras")
plt.ylabel("Cantidad de veces usada")
plt.title("Top 10 palabras más frecuentes en una noticia")

# para mostrar la grafica
plt.show()

"""## Para la distribucion Zipf
Zipf establece que dada una lengua, la frecuencia de aparicion de las distintas palabras de su vocabulario sigue una distribucion que puede aproximarse por:

$P_n \sim 1/n^a$

Tambien se conoce como: "La ley, de manera simple, nos dice que la segunda palabra más usada de un idioma aparecerá la mitad de veces que la palabra más usada, la tercera palabra más usada un tercio de veces que la más usada, la cuarta palabra más usada un cuarto de veces que la más usada, y así sucesivamente."
"""

# ordenamos de mayor a menor
sorted_palabras_contador = dict(sorted(palabras_contador.items(), key=lambda item: item[1], reverse=True))

# se obtiene la lista de palabras y sus frecuencias ordenadas respectivamente
palabras = list(sorted_palabras_contador.keys())
frecuencias = list(sorted_palabras_contador.values())

# se crea una distribución Zipf
dist_zipf = [frecuencias[0] / (i + 1) for i in range(len(frecuencias))]

# se crea una grafica de barras para la distribución de Zipf
plt.bar(np.arange(len(dist_zipf)), dist_zipf, color="green")

# se titula la grafica y los ejes
plt.xlabel("Palabras (ordenadas por frecuencia)")
plt.ylabel("Frecuencia de Zipf")
plt.title("Distribución de Zipf basada en las frecuencias de palabras")

# muestra la grafica
plt.show()

"""## Bibliografia
1.  https://www.madrimasd.org/blogs/matematicas/2019/03/10/146325#:~:text=La%20ley%2C%20de%20manera%20simple,m%C3%A1s%20usada%2C%20y%20as%C3%AD%20sucesivamente.

2. Daniel Jurafsky, James H. Martin. "Speech and Language Processing An Introduction to Natural Language Processing, Computational Linguistics, and Speech Recognition".(2019)
"""
