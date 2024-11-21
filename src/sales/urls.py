from django.urls import path

from .views import SaleCreateView, SaleListView

app_name = 'sales'

urlpatterns = [
    path('', SaleListView.as_view(), name='list'),
    path('create/', SaleCreateView.as_view(), name='create'),
]