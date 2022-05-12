from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Editorial
from .serializer import EditorialSerializer

# Create your views here.
class EditorialList(ListView):
    model=Editorial
    template_name = "editorial/editorial_list.html"


class EditorialDetalle(DetailView):
    model=Editorial
    template_name = "editorial/editorial_detail.html"


class EditorialCreacion(LoginRequiredMixin, CreateView):
    model=Editorial
    success_url = "/editorial"
    fields = ['editorial_name', 'location', 'publication_date']


class EditorialUpdate(LoginRequiredMixin, UpdateView):
    model=Editorial
    success_url = "/editorial"
    fields = ['editorial_name', 'location', 'publication_date']


class EditorialDelete(LoginRequiredMixin, DeleteView):
    model=Editorial
    success_url="/editorial"


class EditorialLista(APIView):
    def get(self, request, format = None):
        editorials = Editorial.objects.all()
        serializer = EditorialSerializer(editorials, many = True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        serializer - EditorialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=HTTP_400_BAD_REQUEST)


class EditorialDetail(APIView):
    def get_object(self, pk):
        try:
            return Editorial.objects.get(pk=pk)
        except Editorial.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format = None):
        editorial = self.get_object(pk)
        serializer = EditorialSerializer(editorial)
        return Response(serializer.data)
    
    def put(self, request, pk, format = None):
        editorial = self.get_object(pk)
        serializer = EditorialSerializer(editorial, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        editorial = self.get_object(pk)
        editorial.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
