# Paso a paso

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
9. creacion del repositorio git 'git init' y primer commit 'git add . && git commit -m "primer commit"'
