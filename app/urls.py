"""TallerDomeyko URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login', views.loginView, name='login'),
    path('logout', views.logoutView, name='logout'),
    path('auth', views.auth, name='auth'),
    path('', views.index, name='index'),
    path('Catalogo/', views.Catalogo, name='catalogo'),
    path('nuevo_trabajo/', views.nuevo_trabajo, name='nuevo_trabajo'),
    path('added_trabajo/', views.added_trabajo, name='added_trabajo'),
    path('add_trabajo', views.add_trabajo, name='add_trabajo'),
    path('nueva_pieza/', views.nueva_pieza, name='nueva_pieza'),
    path('added_pieza/', views.added_pieza, name='added_pieza'),
    path('add_pieza', views.add_pieza, name='add_pieza'),
    path('lista_piezas/' , views.lista_piezas, name='lista_piezas'),
    path('usar_pieza', views.usar_pieza, name='usar_pieza'),
    path('used_pieza', views.used_pieza, name='used_pieza'),
    path('terminar_trabajo', views.terminar_trabajo, name='terminar_trabajo'),
    path('trabajo_terminado/', views.trabajo_terminado, name='trabajo_terminado'),
    path('elsubtotal', views.elsubtotal, name='elsubtotal'),
    path('subtotal/', views.subtotal, name='subtotal'),
    path('sumar_horas', views.sumar_horas, name='sumar_horas'),
    path('add_horas', views.add_horas, name='add_horas'),
    path('abonar', views.abonar, name='abonar'),
    path('abonos_y_subtotales', views.abonos_y_subtotales, name='abonos_y_subtotales'),
    path('venta_directa/', views.venta_directa, name='venta_directa'),
    path('vender_pieza', views.vender_pieza, name='vender_pieza'),
    path('Eliminarcobropieza', views.Eliminarcobropieza, name='Eliminarcobropieza'),
    path('Eliminarcobrohora', views.Eliminarcobrohora, name='Eliminarcobrohora'),
    path('Eliminardeposito', views.Eliminardeposito, name='Eliminardeposito')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
