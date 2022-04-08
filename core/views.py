from django.shortcuts import render

# Create your views here.

def pagina_inicio(request):
    return render(request, 'core/padre.html')

def about_me(request):
    return render(request, 'core/about_me.html')

def contact(request):
    return render(request, 'core/contact.html')