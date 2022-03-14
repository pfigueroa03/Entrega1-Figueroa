from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

from .models import Project, Autor, PublishingCompany
from .forms import ProyectoFormulario, AutorForm, PublishingCompanyForm

# Create your views here.
def proyectos(request):
    projects = Project.objects.all()
    return render (request, 'mainblog/proyectos.html', {'projects':projects})

def proyecto_formulario(request):
    if request.method == "POST":
        form_project = ProyectoFormulario(request.POST)
        print(form_project)

        if form_project.is_valid:
            informacion = form_project.cleaned_data
            projects = Project(project_name=informacion['project_name'], investigation_area=informacion["investigation_area"], description=informacion["description"])
            projects.images = request.FILES.get('images', '')
            projects.save()
            return render(request, "mainblog/proyectos.html")
        
    else:
        form_project = ProyectoFormulario()
        
    return render(request, "mainblog/proyectoFormulario.html", {'form_project':form_project})

def autores(request):
    autors = Autor.objects.all()
    return render (request, 'mainblog/autores.html', {'autors':autors})

def formulario_autores(request):
    if request.method == "POST":
        form_autor = AutorForm(request.POST)
        print(form_autor)

        if form_autor.is_valid:
            informacion = form_autor.cleaned_data
            autors = Autor(firstName=informacion['firstName'], lastName=informacion["lastName"], country=informacion["country"])
            autors.save()
            return render(request, "mainblog/autores.html")
        
    else:
        form_autor = AutorForm()
        
    return render(request, "mainblog/autoresFormulario.html", {'form_autor':form_autor})

def editoriales(request):
    editorials = PublishingCompany.objects.all()
    return render (request, 'mainblog/editoriales.html', {'editorials':editorials})

def formulario_editorial(request):
    if request.method == "POST":
        form_editorial = PublishingCompanyForm(request.POST)
        #print(form_editorial)

        if form_editorial.is_valid:
            informacion = form_editorial.cleaned_data
            editorials = PublishingCompany(publishing_name=informacion['publishing_name'], location=informacion["location"], publication_date=informacion["publication_date"])
            editorials.save()
            return render(request, "mainblog/editoriales.html")
        
    else:
        form_editorial = PublishingCompanyForm()
        
    return render(request, "mainblog/editorialesFormulario.html", {'form_editorial':form_editorial})

def buscar_proyecto(request):
    return render(request, "mainblog/buscarProyecto.html")

def buscar(request):
    if request.GET["nombre"]:
        project_name = request.GET["nombre"]
        proyectos = Project.objects.filter(project_name__icontains=project_name)

        return render (request, "mainblog/resultadoBusqueda.html", {"proyectos": proyectos, "project_name":project_name})
    
    else:
        respuesta = "No se pasaron datos"
    
    return render(request, "mainblog/resultadoBusqueda.html", {"respuesta": respuesta})