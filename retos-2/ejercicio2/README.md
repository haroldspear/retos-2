# retos-2

### Resolución

Se obtiene la frecuencia de los emojis en los posts para cada mes, para realizar histogramas. Se guarda en un diccionario cada mes que tengamos en el dataset, maximo en el rango de un año, el año se define al inicio del archivo py, por el momento es 2019, en todo caso, si se ejecuta normalmente, solo se toma el rango explicado en la sección de ejecución. Las frecuencias se guardan en csvs donde una columna representa el emoji y la segunda columna representa la frecuencia, también se generan gráficos en .png de histogramas del top 10 de emojis.

### Ejecución
Existen 2 formas de ejecución, la normal es la que tiene el filtro de tiempo, es decir, que de todos los posts, que tenemos, se trabaja entre el 1 de mayo al 1 de agosto, y la otra es sin filtro, y se toma todo el dataset, cuando se usa la opción sin filtro, la salida va a la carpeta "output_using_all_data".

Normal (Con filtro):

```
python emojis_histogram_by_month.py
```

Toda la data (Sin filtro):

```
python emojis_histogram_by_month.py --nolimit True
```
