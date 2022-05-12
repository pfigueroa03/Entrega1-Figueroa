#from django.shortcuts import render #, redirect
#from django.urls import reverse
from django.http import Http404 #, HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Project
from .serializer import ProjectSerializer

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


class ProjectList(APIView):
    def get(self, request, format=None):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many = True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetail(APIView):
    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)