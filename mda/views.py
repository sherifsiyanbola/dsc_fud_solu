from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView 
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from mda.forms import MinistryForm
from mda.models import Ministry 

class MinistryCreate(LoginRequiredMixin, CreateView):
    model = Ministry
    form_class = MinistryForm
    success_url = reverse_lazy('mda:ministry_list')


class MinistryDetail(LoginRequiredMixin, DetailView):
    model = Ministry
    
class MinistryList(LoginRequiredMixin, ListView):
    model = Ministry 

class MinistryDelete(LoginRequiredMixin, DeleteView):
    model = Ministry
    success_url = reverse_lazy('mda:ministry_list')

class MinistryUpdate(LoginRequiredMixin, UpdateView):
    model = Ministry
    form_class = MinistryForm
    success_url = reverse_lazy('mda:ministry_list')
