from django.shortcuts import render
from .models import Contactform


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    d = {
        'head': 'Company',
        'des': 'A company, abbreviated as co., is a legal entity representing an association of people, whether '
               'natural, legal or a mixture of both, with a specific objective. Company members share a common purpose '
               'and unite to achieve specific, declared goals.'
    }
    return render(request, 'about.html', d)


def gallery(request):
    return render(request, 'gallery.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        Contactform.objects.create(name=name, email=email, message=message)
        return render(request, 'contact.html')

    else:
        return render(request, 'contact.html')
