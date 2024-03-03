from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from .models import Contact


def index(request):
    return render(request, 'index.html')


def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            last_name = request.POST['last_name']
            phone_number = request.POST['phone_number']
            email = request.POST['email']
            message = request.POST['message']
            contact = Contact(name=name,
                              last_name=last_name,
                              email=email,
                              phone_number=phone_number,
                              message=message,
                              )
            contact.save()
            return HttpResponse('Контакт сохранён')
        return HttpResponse('Ошибка валидации')

    else:
        form = ContactForm()
        message = 'Заполните форму'
        return render(request, 'crypto/add_contact.html', {'form': form, 'message': message})


def show_clients(request):
    contact = Contact.objects.all()
    result = '<br>'.join([str(contact) for contact in contact])
    return HttpResponse(result)
