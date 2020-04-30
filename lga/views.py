from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from lga.forms import LgaForm
from lga.models import Lga 


class LgaCreate(LoginRequiredMixin, CreateView):
    model = Lga
    form_class = LgaForm
    success_url = reverse_lazy('lga:lga_list')


class LgaDetail(LoginRequiredMixin, DetailView):
    model = Lga
    
class LgaList(LoginRequiredMixin, ListView):
    model = Lga 

class LgaDelete(LoginRequiredMixin, DeleteView):
    model = Lga
    success_url = reverse_lazy('lga:lga_list')

class LgaUpdate(LoginRequiredMixin, UpdateView):
    model = Lga
    form_class = LgaForm
    success_url = reverse_lazy('lga:lga_list')
