from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.
def blog(request):
    # carga todos los registros del modelo 'Post'
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {'posts': posts})

def category(request, category_id):
    # carga el registro del modelo 'Category' que concide con el valor de category_id

    # modo sin validar
    # category = Category.objects.get(id=category_id)    

    # modo con validación: get_object_or_404(Modelo, Filtro)
    category = get_object_or_404(Category, id=category_id) 

    return render(request, "blog/category.html", {'category': category})
