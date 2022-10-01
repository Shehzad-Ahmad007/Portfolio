from django.shortcuts import render
from .models import About, Contact, Home, Portfolio, Resume, Service


def index(request):
    homes = Home.objects.all()
    return render(request, 'index.html', {'homes': homes})


def about(request):
    abouts = About.objects.all()
    return render(request, 'about.html', {'abouts': abouts})


def service(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})


def resume(request):
    resumes = Resume.objects.all()
    return render(request, 'resume.html', {'resumes': resumes})


def portfolio(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'portfolio.html', {'portfolios': portfolios})


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        content = request.POST['content']
        contact = Contact(name=name, email=email, content=content)
        contact.save()
    return render(request, 'contact.html')
