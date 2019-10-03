# retos-2

### Resolución

Por cada hashtag base #videogames,#gaming,# nintendoswitch, se obtienen los posts que tienen al menos una palabra palíndroma, y como salida se guarda un csv por cada hashtag base con la data del post, y la palabra palíndroma que se obtuvo del texto del post.

### Ejecución
Existen 2 formas de ejecución, la normal es la que tiene el filtro de tiempo, es decir, que de todos los posts, que tenemos, se trabaja entre el 1 de mayo al 1 de agosto, y la otra es sin filtro, y se toma todo el dataset, cuando se usa la opción sin filtro, la salida va a la carpeta "output_using_all_data".

Normal (Con filtro):

```
python get_posts_with_palindrome.py
```

Toda la data (Sin filtro):

```
python get_posts_with_palindrome.py --nolimit True
```
