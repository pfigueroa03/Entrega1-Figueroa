#from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Autor
from .serializer import AutorSerializer

# Create your views here.
class AutorList(ListView):
    model=Autor
    template_name = "autor/autor_list.html"


class AutorDetalle(DetailView):
    model=Autor
    template_name = "autor/autor_detail.html"


class AutorCreacion(LoginRequiredMixin, CreateView):
    model = Autor
    success_url = "/autor"
    fields = ['firstName', 'lastName', 'country']


class AutorUpdate(LoginRequiredMixin, UpdateView):
    model = Autor
    success_url = "/autor"
    fields = ['firstName', 'lastName', 'country']


class AutorDelete(LoginRequiredMixin, DeleteView):
    model = Autor
    success_url="/autor"


class AutorLista(APIView):
    def get(self, request, format=None):
        autor = Autor.objects.all()
        serializer = AutorSerializer(autor, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AutorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class AutorDetail(APIView):
    def get_object(self, pk):
        try:
            return Autor.objects.get(pk=pk)
        except Autor.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        autor = self.get_object(pk)
        serializer = AutorSerializer(autor)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        autor = self.get_object(pk)
        serializer = AutorSerializer(autor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        autor = self.get_object(pk)
        autor.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)