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

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if "Hx-Request" in request.headers:
            return self.render_clients_autocomplete(request)
        return super().get(request, *args, **kwargs)

    def render_clients_autocomplete(self, request: HttpRequest) -> HttpResponse:
        clients_list = Client.objects.all()
        wanted_client = request.GET.get("client_name", "")
        if not wanted_client.strip() == "": 
            clients_list = Client.filter_by_name(wanted_client, clients_list)
        return render(request, 'sales/components/clients_autocomplete.html', {'clients_list': clients_list})

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        _ = super().form_valid(form)
        messages.success(self.request, 'Nouvelle vente enrégistrée.')
        return redirect('sales:create')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clients_list'] = Client.objects.all()
        return context

    
class SaleListView(ListView):
    model = Sale
    template_name = 'sales/list.html'
    context_object_name = 'sales'
