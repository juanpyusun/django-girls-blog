# Proyecto Django

## Índice

- [Proyecto Django](#proyecto-django)
  - [Índice](#índice)
  - [Instalacion y configuracion del proyecto](#instalacion-y-configuracion-del-proyecto)
  - [Descripcion del proyecto](#descripcion-del-proyecto)
  - [Despliegue en PythonAnywhere](#despliegue-en-pythonanywhere)
  - [Interfaz Grafica y URLs](#interfaz-grafica-y-urls)

## Instalacion y configuracion del proyecto

1. creacion README.md
2. creacion de entorno virtual limpio de librerias `python -m virtualenv --clear .venv`
3. acceder al entorno virtual, hay dos maneras, desde consola o usando vscode directamente
   - consola: `source .venv/bin/activate` (linux) o `.venv\Scripts\activate` (windows)
   - vscode: ctrl+shift+p -> python: select interpreter -> seleccionar el entorno virtual creado y abrir una nueva terminal
   - En ambos casos, el prompt de la terminal debe cambiar para indicar que el entorno virtual esta activo, en nuestro caso `.venv`
4. instalacion de librerias necesarias, en este caso django `pip install django`
5. creacion archivo requirements.txt con las librerias instaladas `pip freeze > requirements.txt`
6. creacion archivo .gitignore para evitar subir al repositorio archivos innecesarios, se sacara un .gitignore de ejemplo de la pagina gitignore.io
7. creacion del archivo .ENV para guardar variables de entorno
8. creacion del proyecto django `django-admin startproject config .`
9. creacion del repositorio git `git init` y primer commit `git add .` y finalmente `git commit -m "primer commit"`
10. Configuraciones iniciales del proyecto en config/settings.py
    - cambio de idioma a español colombiano `LANGUAGE_CODE = 'es-CO'`
    - configuracion de zona horaria `TIME_ZONE = 'America/Bogota'`
    - configuracion de hosts permitidos `ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']`
    - configuracion de la ruta estatica `STATIC_ROOT = BASE_DIR / `static``
    - configuracion de la base de datos `DATABASES = {`default`: {`ENGINE`: `django.db.backends.sqlite3`, `NAME`: BASE_DIR / `db.sqlite3`,}}`
    - Creacion de la base de datos con `python manage.py migrate`, esta ya está definida por defecto en django
11. Ejecucion del servidor de desarrollo `python manage.py runserver` y verificacion en el navegador en la direccion `<http://127.0.0.1:8000/>`, debe aparecer la pagina de bienvenida de django, ademas podemos acceder a la administracion en `<http://127.0.0.1:8000/admin/>`, donde podremos gestionar nuestro sitio.
12. Configuracion usuario administrador con `python manage.py createsuperuser` y seguir los pasos para crear el usuario.

## Descripcion del proyecto

Este proyecto es un blog basico desarrollado con Django, que permite a los usuarios crear, editar y eliminar publicaciones. Ademas, cuenta con un sistema de autenticacion para gestionar el acceso a la administracion del sitio.

1. Crear aplicacion principal del blog con `python manage.py startapp blog`
2. Agregar la aplicacion al proyecto en config/settings.py en la seccion INSTALLED_APPS
3. Crear el modelo Post en blog/models.py como una clase que hereda de models.Model con los siguientes campos:
    - author: ForeignKey al modelo User de Django (ya creado)
    - title: CharField con max_length=200
    - text: TextField para el contenido del post
    - created_date: DateTimeField con auto_now_add=True
    - published_date: DateTimeField con null=True, blank=True
    - definir el metodo publish para publicar el post
    - definir el metodo __str__ para representar el post por su titulo
4. añadir el modelo Post a la administracion de Django en blog/admin.py
5. crear y aplicar migraciones con `python manage.py makemigrations blog` y `python manage.py migrate blog`
6. comprobar en la administracion de Django que el modelo Post aparece correctamente y se pueden crear, editar y eliminar posts.

## Despliegue en PythonAnywhere

1. Crear una cuenta en PythonAnywhere
2. Subir el proyecto a un repositorio en GitHub
3. En PythonAnywhere crear una consola bash
4. Instalar un script para automatizar el despliegue `pip3.6 install --user pythonanywhere` y ejecutarlo `pa_autoconfigure_django.py --python=3.6 <https://github.com/usuario-github/url_del_repositorio.git>`
5. Comprobar que el sitio web funciona correctamente accediendo a la URL proporcionada por PythonAnywhere.

## Interfaz Grafica y URLs

1. Agregar las URLs de la aplicacion del blog al proyecto principal en config/urls.py, para que asi reconozca las urls definidas en la app del blog
2. Se crea el archivo blog/urls.py para definir las rutas especificas del blog, como la vista principal que muestra los posts publicados.
3. se crea la vista, una funcion, post_list en blog/views.py que renderiza la plantilla blog/post_list.html para mostrar la lista de posts.
4. 