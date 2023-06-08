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
    path('tareas/', views.tareas, name='tareas'),
    path('tareas/create/', views.tareas_create, name='tareas_create'),
    path('tareas/<int:id>/', views.tarea_detail, name='tarea_detail'),
    path('tareas/<int:id>/edit', views.tarea_edit, name='tarea_edit'),
    path('tareas/<int:id>/remove', views.tarea_remove, name='tarea_remove'),
    path('tareas/<str:letra>/', views.filtrado_por_letra, name='filtrado_por_letra'),
]
