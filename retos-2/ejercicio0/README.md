# retos-2

### Resolución

En este ejercicio se obtienen otros hashtag aparte de #videogames,#gaming y # nintendoswitch, que pueden servir para obtener mas likes y mas comments.

Consiste en tomar la cantidad de likes y comments que tiene asociado cada hastag en los posts, sumar todo y luego dividir el resultado entre la cantidad de post, esto quiere decir, por ejemplo, que si un hastag #A tiene acumulado 10000 likes y otro #B tiene acumulado, 3000, no necesariamente el de 10000 es un mejor hashtag, ya que si el primero #A fue publicado 1000 veces la relación es 10000/1000, que son 10 likes por post, y el otro #B ha sido posteado  10 veces, no es un hastag tan común y su relacion es 3000/10, que son 300 likes por post. Dejando como resultado que #B es un mejor hashtag, que podríamos usar para nuestros nuevos posts.

### Ejecución
Existen 2 formas de ejecución, la normal es la que tiene el filtro de tiempo, es decir, que de todos los posts, que tenemos, se trabaja entre el 1 de mayo al 1 de agosto, y la otra es sin filtro, y se toma todo el dataset, cuando se usa la opción sin filtro, la salida va a la carpeta "output_using_all_data".

Normal (Con filtro):

```
python get_best_hashtags.py
```

Toda la data (Sin filtro):

```
python get_best_hashtags.py --nolimit True
```
