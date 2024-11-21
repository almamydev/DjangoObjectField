from django.contrib import admin
from django.urls import path, include

from DjangoHtmx.views import index

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('sales/', include('sales.urls')),
]
