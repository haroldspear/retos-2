# retos-2

### Resolución

Para cada año, mes y día que se tiene en el dataset se obtiene el top 20 de usuarios que postearon más veces un determinado hashtag #videogames,#gaming o # nintendoswitch, se crearon 3 diccionarios generales, uno contiene los años, otro los meses y uno con los días, estos a su vez tienen un diccionario donde están los hashtag y dentro de este los users que lo postearon con la respectiva cantidad de veces, que fue posteado, con esto se hace un ordenamiento y se toma los primeros 20, para obtener el top.

### Ejecución
Existen 2 formas de ejecución, la normal es la que tiene el filtro de tiempo, es decir, que de todos los posts, que tenemos, se trabaja entre el 1 de mayo al 1 de agosto, y la otra es sin filtro, y se toma todo el dataset, cuando se usa la opción sin filtro, la salida va a la carpeta "output_using_all_data".

Normal (Con filtro):

```
python top_20_handles.py
```

Toda la data (Sin filtro):

```
python top_20_handles.py --nolimit True
```
