from django.urls import path
from . import views

urlpatterns = [
    path('', views.random_quotes),
    #path(r'^mensaje/',views.mensaje)
]
