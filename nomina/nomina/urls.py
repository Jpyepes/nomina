"""nomina URL Configuration

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
from core import views as coreViews
from produccion import views as produccionViews
from login import views as loginViews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginViews.login, name='login'),
    path('landing/', coreViews.landing, name='landing'),
    path('calcularNomina/', coreViews.form, name='form'),
    path('crearEmpleado/', coreViews.crearEmpleado, name='crearEmpleado'),
    path('actualizarEmpleado/', coreViews.actualizarEmpleado, name='actualizarEmpleado'),
    path('historialNomina/', coreViews.historialNomina, name='historialNomina'),
    path('crearProducto/', produccionViews.crearProducto, name='crearProducto'),
    path('crearOrden/', produccionViews.crearOrden, name='crearOrden'),
    path('verOrden/', produccionViews.verOrden, name='verOrden'),
    path('verPedido/', produccionViews.verPedido, name='verPedido'),
    path('inventario/', produccionViews.inventario, name='inventario'),
]
