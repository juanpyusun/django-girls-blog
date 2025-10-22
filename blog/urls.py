from django.urls import path
from . import views

# Definimos las rutas especificas de la aplicacion del blog
# En este caso, solo tenemos la ruta raiz que muestra la lista de posts
# Cada que alguien entre a "localhost:8000/" se le dirigira a la vista index
# que se encuentra en views.py y se le asigna el nombre 'index' para referenciarla facilmente
urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit')
]