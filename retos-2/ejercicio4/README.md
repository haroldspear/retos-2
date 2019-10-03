# retos-2

### Resolución

Usando los 3 hastags que tenemos como base #videogames,#gaming y # nintendoswitch, se obtuvieron otros hashtags que estaban en los mismos posts que estaban junto con alguno o algunos de los 3. Con esto, se hizo una intersección entre los hashtags que se obtuvieron, por cada hashtag base y esa intersección es la salida de este ejercicio, esto se hace por cada mes, máximo en el rango de un año, definido como 2019, esto es si se usa toda la data.

### Ejecución
Existen 2 formas de ejecución, la normal es la que tiene el filtro de tiempo, es decir, que de todos los posts, que tenemos, se trabaja entre el 1 de mayo al 1 de agosto, y la otra es sin filtro, y se toma todo el dataset, cuando se usa la opción sin filtro, la salida va a la carpeta "output_using_all_data".

Normal (Con filtro):

```
python overlap_hashtags.py
```

Toda la data (Sin filtro):

```
python overlap_hashtags.py --nolimit True
```
