from django.shortcuts import render

def index(request):
    return render(request, 'website/index.html')

def menu(request):
    return render(request, 'website/menu.html')

def administration(request):
    return render(request, 'website/administration.html')

def contact(request):
    return render(request, 'website/contact.html')