from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Editorial

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
