# PruebaQuick
### _API Rest en Django para prueba de cargo de desarrollador para QUICK_
 La aplicación se encuentra montada sobre el Framework Django (Python), e implementa la librería [djangorestframework](https://www.django-rest-framework.org/), además hace uso del manejo de sentencias sql para importar y exportar archivos CSV con información almacenada en la base de datos [sqlite3](https://sqlite.org/index.html)

[![N|Solid](https://static.djangoproject.com/img/logos/django-logo-negative.svg)](https://www.djangoproject.com/)

# PROBLEMA

Se debe desarrollar un REST API que permita realizar operaciones CRUD en las entidades de Cliente, Facturas y Productos.
Adicional al CRUD de cada entidad, se debe proporcionar:
- Un endpoint que permita registrar a un usuario con correo electrónico y contraseña.
- Un endpoint que permita iniciar sesión con el correo electrónico y contraseña previamente creados, generando un JSON Web Token.
- Que los endpoints de entidades estén asegurados por un JSON Web Token recibido desde la cabecera de la petición.
- Un endpoint que permita realizar la descarga de un archivo CSV con la lista de registros de Cliente: mostrando documento, nombre completo y la cantidad facturas relacionadas.
- Un endpoint que permita realizar el cargue de un archivo CSV con resgitros para la creacion de Clientes.
- Usar el ORM de Django para las consultas de Productos y para el resto usar SQL plano en lo posible.





## Instalación del proyecto

Antes de descargar el proyecto del repositorio, asegúrese tener instalado Python3, y que este se encuentre agregado en las variables de entorno del sistema para garantizar que los comandos requeridos para la instalación de los paquetes se ejecuten de la forma correcta

Se recomienda utilizar un ambiente virtual de Python, para evitar conflictos con las versiones de los paquetes.
Para crear el ambiente virtual abra una ventana de comandos y dirigase a la carpeta donde se encuentra el proyecto, y ejecute el siguiente comando en la terminal de Powershell o bash según aplique:

```
python3 -m venv venv
```
_Dado que el proyecto fue creado en Windows, los comandos utilizados aplican para Powershell._

Activar el ambiente virtual
```
.\venv\Scripts\activate
```

Una vez habilitado el ambiente virtual, proceda a instalar los paquetes de Python requeridos para el proyecto, el archivo de requerimientos se encuentra dentro del proyecto:
```
pip install -r requirements.txt
```

## Paquetes
Los principales paquetes usados en el proyecto son:

| Paquete | Link |
| ------ | ------ |
| Django | https://pypi.org/project/Django/ |
| Django REST Framework | https://pypi.org/project/djangorestframework/ |
| Pandas | https://pypi.org/project/pandas/ |

Una vez instalados los paquetes necesarios, dirígase a la carpeta del proyecto Django y ejecute los siguientes comandos para inicializar la base de datos del proyecto:
```
python manage.py makemigrations
python manage.py migrate
```

Una vez creados los modelos en la base de datos, ejecute el siguiente código para iniciar el servicio para la API REST, esto lanzará el servicio de manera local en el puerto 8000 por defecto:
```
python manage.py runserver
```
Debería ver el siguiente mensaje en la ventana de comandos:
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
December 22, 2021 - 01:50:25
Django version 3.2.10, using settings 'QuickTest.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```