from django.shortcuts import render

# Create your views here.

# Se ha creado la vista post_list que recibe una solicitud (request)
# y devuelve el renderizado de la plantilla 'blog/post_list.html'

def post_list(request):
    return render(request, 'blog/post_list.html', {})