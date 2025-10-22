# Proyecto Django
## Índice

- [Proyecto Django](#proyecto-django)
  - [Índice](#índice)
  - [Instalacion y configuracion del proyecto](#instalacion-y-configuracion-del-proyecto)
  - [Descripcion del proyecto](#descripcion-del-proyecto)

## Instalacion y configuracion del proyecto

1. creacion README.md
2. creacion de entorno virtual limpio de librerias 'python -m virtualenv --clear .venv'
3. acceder al entorno virtual, hay dos maneras, desde consola o usando vscode directamente
   - consola: 'source .venv/bin/activate' (linux) o '.venv\Scripts\activate' (windows)
   - vscode: ctrl+shift+p -> python: select interpreter -> seleccionar el entorno virtual creado y abrir una nueva terminal
   - En ambos casos, el prompt de la terminal debe cambiar para indicar que el entorno virtual esta activo, en nuestro caso '.venv'
4. instalacion de librerias necesarias, en este caso django 'pip install django'
5. creacion archivo requirements.txt con las librerias instaladas 'pip freeze > requirements.txt'
6. creacion archivo .gitignore para evitar subir al repositorio archivos innecesarios, se sacara un .gitignore de ejemplo de la pagina gitignore.io
7. creacion del archivo .ENV para guardar variables de entorno
8. creacion del proyecto django 'django-admin startproject config .'
9. creacion del repositorio git 'git init' y primer commit 'git add .' y finalmente 'git commit -m "primer commit"'
10. Configuraciones iniciales del proyecto en config/settings.py
    - cambio de idioma a español colombiano 'LANGUAGE_CODE = 'es-co''
    - configuracion de zona horaria 'TIME_ZONE = 'America/Bogota''
    - configuracion de hosts permitidos 'ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']'
    - configuracion de la ruta estatica 'STATIC_ROOT = BASE_DIR / 'static''
    - configuracion de la base de datos 'DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': BASE_DIR / 'db.sqlite3',}}'
    - Creacion de la base de datos con 'python manage.py migrate', esta ya está definida por defecto en django
11. Ejecucion del servidor de desarrollo 'python manage.py runserver' y verificacion en el navegador en la direccion 'http://127.0.0.1:8000/', debe aparecer la pagina de bienvenida de django, ademas podemos acceder a la administracion en 'http://127.0.0.1:8000/admin/', donde podremos gestionar nuestro sitio.
12. Configuracion usuario administrador con 'python manage.py createsuperuser' y seguir los pasos para crear el usuario.

## Descripcion del proyecto
