
from django.contrib import admin
from django.urls import path
from inicio.views import inicio

urlpatterns = [
    path('', inicio, name='inicio'),
    path('admin/', admin.site.urls),
]
