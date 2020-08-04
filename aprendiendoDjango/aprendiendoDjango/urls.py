"""aprendiendoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# improtar mis vistas
from miapp import views

# URLS
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola-mundo/', views.holaMundo, name='hola'),
    path('index/', views.index, name="index"),
    path('contacto/', views.contacto, name="contacto"),
    path('prueba/', views.prueba, name="prueba"),
    path('', views.index, name="inicio"),
    path('crear-articulo/<str:title>/<str:content>/<str:public>/', views.crearArticulo, name='article'),
    path('articulo/', views.articulo, name="articulo"),
    path('editar-articulo/<int:id>', views.editarArticulo, name="edit"),
    path('articulos/', views.articulos, name="articulos"),
    path('borrar-articulo/<int:id>/', views.borrarArticulo, name='eliminar'),
    path('save-article/', views.save_article, name = 'save'),
    path('create-article/', views.create_article, name = 'create'),
    path('create-class/', views.create_artcile_class, name = 'class'),

]
