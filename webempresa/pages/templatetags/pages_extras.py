# el nombre del fichero 'pages_extras.py' es el que nosotros queramos

# importamos la libreria de template 
from django import template

# importamos nuestro modelo de 'Page' de la app 'pages'
from pages.models import Page 

# definimos una instancia de la libreria de templates
register = template.Library()

# vamos ahora a definir a la función 'get_page_list' para que actue como un 'template tag',
# utilizando para ello la siguiente función decoradora
@register.simple_tag

# esta función actua como 'template tag' para recuperar todos los registros del modelo 'Page'. 
# este se utiliza en el template 'base.html', en el footer apartado de 'avisos'.
def get_page_list():
    pages = Page.objects.all()
    return pages
