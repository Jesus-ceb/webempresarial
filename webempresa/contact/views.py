from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.


def contact(request):
    contact_form = ContactForm()
    
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            
            # Enviamos el correo y redireccionamos
            email = EmailMessage(
                "la Cafetteria: nuevo mensaje de contacto",
                "De {} <{}> \n\nEscribio:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["jesusarley9413@hotmail.com"],
                reply_to=[email]
            )
            
            try:
                email.send()
                # algo no ah ido bien redireccionamos a Ok
                return redirect(reverse('contact')+"?ok")
            except:
                # algo no ah ido bien redireccionamos a Fail
                return redirect(reverse('contact')+"?fail")
    
    return render(request, "contact/contact.html", {'form':contact_form})
