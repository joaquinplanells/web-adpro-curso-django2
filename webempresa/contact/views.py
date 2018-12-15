from django.shortcuts import render, redirect # redirect es para redireccionar páginas

from django.urls import reverse # nos permite hacer una redirección para pasar los datos ocultos

from django.core.mail import EmailMessage # nos permite crear la estructura de un mensaje y enviar el correo

# importamos el modelo 'ContactForm()'
from .forms import ContactForm

# Create your views here.
def contact(request):

    # instanciamos el modelo 'ContactForm()' sin datos
    contact_form = ContactForm()

    # verificamos que el método de envio sea post
    if request.method == "POST":

        # instanciamos el modelo 'ContactForm()' con los datos a enviar
        contact_form = ContactForm(data=request.POST)

        # verificamos que todos los campos son correctos
        if contact_form.is_valid():

            # recuperamos el valor de los campos en las variables
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            # Enviamos el correo y redireccionamos: https://mailtrap.io/
            email = EmailMessage(
                    "La Caffettiera: Nuevo mensaje de contacto",                          # asunto
                    "De {} <{}> \n\n Escribió:\n\n {} ".format(name, email, content),     # cuerpo
                    "no-contestar@inbox.mailtrap.io",                                     # email_origen
                    ["joaquinplanells@gmail.com"],                                        # email_destino
                    reply_to=[email]
            )

            # función send() para enviar el correo
            try:
                email.send()
                # TODO ha ido bien, redireccionamos a OK (reverse oculta los datos )
                return redirect(reverse('contact')+"?ok")
            except:
                # algo no ha ido bien, redireccionamos a FAIL (reverse oculta los datos )
                return redirect(reverse('contact')+"?fail")

    # enviamos al template la instancia del modelo 'ContactForm()' -> {'form':contact_form}
    return render(request, "contact/contact.html", {'form':contact_form})
