from django.shortcuts import render

# Create your views here.

# Se ha creado la vista index que recibe una solicitud (request)
# y devuelve el renderizado de la plantilla 'templates/blog/index.html'

# El tercer parametro es un diccionario que puede enviar datos a la plantilla, en este caso esta vacio
# ademas reconoce automaticamente la carpeta templates/ como el origen de las plantillas dinamicas para esta app
def index(request):
    return render(request, 'blog/index.html', {}) 