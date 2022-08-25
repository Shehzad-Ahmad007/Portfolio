from django.shortcuts import render
from .models import About, Contact, Home


def index(request):
    homes = Home.objects.all()
    return render(request, 'index.html', {'homes': homes})


def about(request):
    abouts = About.objects.all()
    return render(request, 'about.html', {'abouts': abouts})


def service(request):
    return render(request, 'services.html')


def resume(request):
    return render(request, 'resume.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        content = request.POST['content']
        contact = Contact(name=name, email=email, content=content)
        contact.save()
    return render(request, 'contact.html')
