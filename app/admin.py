from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Auto)
admin.site.register(Trabajo)
admin.site.register(Horas)
admin.site.register(Depositos)
admin.site.register(Piezas_usadas)
admin.site.register(Piezas_en_inventario)
admin.site.register(Usos)
admin.site.register(PiezaUso)
admin.site.register(Ventas)