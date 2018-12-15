from .models import Link

def ctx_dict(request):
    #definimos un diccionario
    ctx = {}

    #cargamos todos los registros en la lista 'links'
    links = Link.objects.all()

    #guardamos los elementos de la lista en el diccionario 'ctx'
    for link in links:
        ctx[link.key] = link.url
        
    return ctx
