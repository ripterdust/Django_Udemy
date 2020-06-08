from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article, Category


# Create your views here.

def index(request):

    lenguajes = ['Javascript', 'CSS', 'Python', 'SQL']
    return render(request, 'index.html', {
        'title': 'Inicio',
        'miVariable': 'Esta es una variable.',
        'lenguajes': lenguajes,
        'nombre': 'Bryan Arévalo'
    })

def holaMundo(request):
    nombre = 'Bryan Arévalo'
    return render(request, 'hola_mundo.html', {
        'title': 'Hola mundo',
        'nombre': nombre
    })

def contacto(request, nombre="Bryan", apellido="Arévalo"):
    return HttpResponse(f'<h2>Página de contacto.</h2><br/><h1>{nombre} {apellido}</h1>')

def prueba(request):
    
    return render(request, 'pagina.html', {
        'title': 'Prueba'
    })

def crearArticulo(request, title, content, public):
    articulo = Article(
        title = title,
        content = content,
        public = public
    )

    articulo.save()
    return HttpResponse(f'Artículo creado: { articulo.title } - { articulo.content }')

def articulo(request):

    try: 
        articulo = Article.objects.get(title='Super man', public=False)

        return HttpResponse(f'Artículo: { articulo.id } - { articulo.title } - { articulo.content }')
    except:
        return HttpResponse('Artículo no encontrado')

def editarArticulo(request, id):

    try: 
        articulo =  Article.objects.get(pk=id)
        articulo.title = 'Badman'
        articulo.content = 'Película del 2017'
        articulo.public = False
        articulo.save()
        return HttpResponse('Artículo editado.')
    except:
        return HttpResponse('Ha ocurrido un error, prueba más tarde.')

def articulos(request):
    # Esto los ordena por id y solo obtiene 5
    # articulos = Article.objects.order_by('id')[:5]
    articulos = Article.objects.all()

    return render(request, 'articulos.html', { 
        'articulos': articulos,
        'title': 'Artículos'
        })

def borrarArticulo(request, id):
    # Esta función borra un solo artículo
    articulo = Article.objects.get(pk=id)
    articulo.delete()

    return redirect('articulos')
