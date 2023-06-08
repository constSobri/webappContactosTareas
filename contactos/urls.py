"""personal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('contactos/', views.contactos, name='contactos'),
    path('contactos/create/', views.contactos_create, name='contactos_create'),
    path('contactos/<int:id>/', views.contactos_detail, name='contactos_detail'),
    path('contactos/<int:id>/edit/', views.contactos_edit, name='contactos_edit'),
    path('contactos/<int:id>/remove/', views.contactos_remove, name='contactos_remove'),
    path('contactos/<str:letra>/', views.filtrado_por_letra, name='filtrado_por_letra'),
]
