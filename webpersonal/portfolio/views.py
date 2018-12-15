from django.shortcuts import render
from .models import Project # importamos 'models' en el mismo directorio con el '.'' delante

# Create your views here.
def portafolio(request):
	# creamos una lista para almacenar todos los registros de la tabla 'Project' utilizando 
	# el método all()
    projects = Project.objects.all()
    # en el método render especificamos el template 'portfolio.html' y los registros
    # de la tabla 'Project' con  el diccionario {'projects':projects} con lo que se renderizara
    # la página a visualizar mediante el navegador
    return render(request, "portfolio/portafolio.html", {'projects':projects})
