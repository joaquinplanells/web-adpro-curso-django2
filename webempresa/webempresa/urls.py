"""webempresa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include


# para poder acceder al 'settings.DEBUG' -> (1)
from django.conf import settings


urlpatterns = [
    # path del core
    path('', include('core.urls')),
    # path del services: poner siempre la barra '/'
    path('services/', include('services.urls')),
    # path del contact: poner siempre la barra '/'
    path('contact/', include('contact.urls')),
    # path del blog: poner siempre la barra '/'
    path('blog/', include('blog.urls')),
    # path del pages: poner siempre la barra '/'
    path('page/', include('pages.urls')),
    # path del admin
    path('admin/', admin.site.urls),
]

# (1) solo funciona en modo debug para servir imagenes estaticas (se utiliza solo en la fase de desarrollo)
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Custom title for admin
admin.site.site_header = "La Caffetiera"
admin.site.index_title = "Panel de administración"
admin.site.site_title = "La Caffetiera"
