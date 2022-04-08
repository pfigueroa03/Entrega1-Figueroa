from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Autor

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
