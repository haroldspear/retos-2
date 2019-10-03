# retos-2

### Prerequisites

Tener instalada una versión de python 3, las pruebas se realizaron  en python 3.6. Se recomienda usar un ambiente virtual, para no sobreescribir las dependencias que se van a instalar.

```
pip install -r requirements.txt
```

## Ejecución de los ejercicios
Para obtener los datos, se usa get_data.py, que tiene como parámetros, el user, pass y el hashtag en específico a obtener, ya que para que se descarguen paralelamente se pueden usar 2 cuentas extra:

Recurso:
* instagramapi22@gmail.com,instagramapi44
* haroldapiinstagram@gmail.com,instagramapi44

Ejecución, con parámetros por defecto, ya tiene una cuenta predefinida y se usará el mismo proceso, para obtener la data de cada hashtag.

```
python get_data.py
```

Ejecución en paralelo:

```
python get_data.py -u instagramapi22@gmail.com -p instagramapi44 -ha gaming
```

Ejecución de los ejercicios:

Está especificada en el README de cada carpeta, donde se encuentran los ejercicios, ejercicioN

## Notas
* El ejercicio 1 toma los comentarios (No el texto del post) de todos los post que tengo y obtiene los sentimientos.

* Los ejercicios tienen una carpeta de salida general en (output_all_data), donde se obtendrá la salida si se usab como entrada todos los datos del dataset.

* Si se van a descargar nuevos datos, respaldar la carpeta "data", para probar los ejercicios, con data ya descargada
