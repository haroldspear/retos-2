# retos-2

### Prerequisites

Tener instalada una versión de python 3, las pruebas se realizaron  en python 3.6. Se recomienda usar un ambiente virtual, para no sobreescribir las dependencias que se van a instalar.

```
pip install -r requirements.txt
```

## Ejecución de los ejercicios
Para obtener los datos, se usa get_data.py, hay mas de uno porque se usó paralelamente con diferentes cuentas para que cada una baje un hashtag, no está parametrizado
```
python get_data.py
```

```
python ejercicioN.py
```

## Notas
* El ejercicio 1 toma los comentarios de todos los post que tengo y obtiene los sentimientos.

* El ejercicio 3 y 5 tienen una carpeta de salida en(output_all_data), de tal manera que se usa como entrada todos los datos.

* Si se van a descargar nuevos datos, respaldar la carpeta "data", para probar los ejercicios, con data ya descargada
