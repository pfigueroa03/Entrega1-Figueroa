from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Project

# Create your views here.
#Vistas basada en Clase
class ProyectoList(ListView):
    model=Project
    template_name = "mainblog/proyecto_lista.html"


class ProyectoDetalle(DetailView):
    model=Project
    template_name = "mainblog/proyecto_detalle.html"


class ProyectoCreacion(LoginRequiredMixin, CreateView):
    model = Project
    success_url = "/pages"
    fields = ['project_name', 'subtitle', 'investigation_area', 'summary', 'autor', 'images', 'description']


class ProyectoUpdate(LoginRequiredMixin, UpdateView):
    model = Project
    success_url = "/pages"
    fields = ['project_name', 'subtitle', 'investigation_area', 'summary', 'autor', 'images', 'description']


class ProyectoDelete(LoginRequiredMixin, DeleteView):
    model = Project
    success_url="/pages"