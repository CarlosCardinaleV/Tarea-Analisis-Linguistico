# Tarea-Analisis-Linguistico

# Análisis Lingüístico en Python

Este repositorio contiene un proyecto que realiza un análisis lingüístico de una página web en español utilizando Python. A continuación, se describen los aspectos clave de este proyecto.

## Descripción

En este proyecto, se realiza un análisis lingüístico de una página web en español utilizando Python. Las tareas principales incluyen la identificación y extracción de oraciones y tokens, el manejo de caracteres especiales y la aplicación de la teoría del tamaño del vocabulario.

## Proceso de Análisis

### Identificación de Oraciones

1. Se limpia el formato HTML de la página para facilitar la identificación de las oraciones.
2. Se utilizan expresiones regulares para identificar y extraer las oraciones claramente del texto.

### Identificación de Tokens

1. Los tokens se refieren a las palabras dentro de las oraciones.
2. Se extraen fácilmente mediante el uso de expresiones regulares.

### Caracteres Especiales

No se hace distinción entre los caracteres especiales del español.
Expresiones regulares generales se utilizan para tener en cuenta todos los caracteres.

### Expresiones Regulares Utilizadas

- Para extraer oraciones: `r'.*.'`
- Para extraer palabras de las oraciones: `r'\w+'`

### Tamaño del Vocabulario

Según la teoría, a medida que el texto se vuelve más grande, aumenta la cantidad de palabras distintas en el documento. Esto se comporta de acuerdo con la ley de Herdan.

## Análisis de Frecuencia

1. Se muestra la frecuencia de cada término en el vocabulario, ordenados de mayor a menor frecuencia.

2. Se incluye una gráfica que representa la distribución de la frecuencia de términos.

## Distribución de Zipf

La distribución de Zipf establece que las palabras más utilizadas aparecerán con mayor frecuencia que las menos utilizadas. Esto se describe de la siguiente manera: "La segunda palabra más usada aparecerá la mitad de veces que la palabra más usada, la tercera palabra más usada un tercio de veces que la más usada, la cuarta palabra más usada un cuarto de veces que la más usada, y así sucesivamente." (1)

## Contribución

Si deseas contribuir a este proyecto, por favor sigue las pautas descritas en el archivo CONTRIBUTING.md.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE.md para obtener más detalles.
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

---
## Bibliografía

[(1) La ley de Zipf revisitada](https://www.madrimasd.org/blogs/matematicas/2019/03/10/146325#:~:text=La%20ley%2C%20de%20manera%20simple,m%C3%A1s%20usada%2C%20y%20as%C3%AD%20sucesivamente.)