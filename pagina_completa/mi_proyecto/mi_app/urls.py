from django.urls import path
from . import views
from django.contrib import admin
from .views import contacto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('contacto/', views.contacto, name='contacto'),
    path('escuela/', views.escuela, name='escuela'),
    path('musica/', views.musica, name='musica'),
    path('gracias/', views.gracias, name='gracias'),
]