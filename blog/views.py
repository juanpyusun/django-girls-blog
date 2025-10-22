from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.

# Se ha creado la vista index que recibe una solicitud (request)
# y devuelve el renderizado de la plantilla 'templates/blog/index.html'

# El tercer parametro es un diccionario que puede enviar datos a la plantilla, en este caso esta vacio
# ademas reconoce automaticamente la carpeta templates/ como el origen de las plantillas dinamicas para esta app
def index(request):
    # el atributo __lte significa 'less than or equal to' (menor o igual que)
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/index.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})