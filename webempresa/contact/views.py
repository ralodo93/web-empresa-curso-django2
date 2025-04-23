from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
# Create your views here.

def contact(request):
    print(f"Tipo de petición: {request.method}")
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get("name", "")
            email = request.POST.get("email", "")
            message = request.POST.get("message", "")
            # enviamos el correo y redireccionamos
            email = EmailMessage(
                #asunto
                "La Caffettiera: Nuevo mensaje de contacto",
                #cuerpo
                f"De {name} <{email}>\n\nEscribió:\n\n{message}",
                # origen
                "no-reply@inbox.mailtrap.io",
                #destinatario
                ["raullopezdominguez@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse("contact") + "?ok")
            except:
                return redirect(reverse("contact") + "?fail")
            
    return render(request, "contact/contact.html", {"form": contact_form})