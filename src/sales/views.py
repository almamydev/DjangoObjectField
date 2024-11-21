from email import message
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView
from django.contrib import messages
from django.urls import reverse_lazy

from .models import Sale
from clients.models import Client


class SaleCreateView(CreateView):
    model = Sale
    fields = ['sale_date', 'client', 'product']
    template_name = 'sales/create.html'
    success_url = reverse_lazy('sales:create')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        _ = super().form_valid(form)
        messages.success(self.request, 'Nouvelle vente enrégistrée.')
        return redirect('sales:create')
    
    
class SaleListView(ListView):
    model = Sale
    template_name = 'sales/list.html'
    context_object_name = 'sales'