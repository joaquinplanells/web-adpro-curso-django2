from django.shortcuts import render, get_object_or_404
from .models import Page

# Create your views here.
def page(request, page_id, page_slug):
    # carga el registro del modelo 'Page' que concide con el valor de page_id y del page_slug
    page = get_object_or_404(Page, id=page_id)
    return render(request, "pages/aviso.html", {'page': page})
