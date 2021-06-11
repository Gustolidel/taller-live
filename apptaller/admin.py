from django.contrib import admin
from .models import Conductor,Repuesto, JefeAlmacen, Tecnico, Marca, Camion,  Pedido, Administrador, Diagnostico, Recepcionista
# Register your models here.
admin.site.register(Repuesto)
admin.site.register(JefeAlmacen)
admin.site.register(Pedido)
admin.site.register(Tecnico)
admin.site.register(Marca)
admin.site.register(Camion)
admin.site.register(Administrador)
admin.site.register(Diagnostico)
admin.site.register(Recepcionista)
admin.site.register(Conductor)
