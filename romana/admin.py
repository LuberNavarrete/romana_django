from django.contrib import admin
from .models import chofer, romana

class choferadmin(admin.ModelAdmin):
        search_fields = ['ci','nombre']
        list_display = ('ci','nombre','placa_vehiculo','modificado','observacion','activo')
        list_filter = ['activo','nombre']

admin.site.register(chofer,choferadmin)

class romanaadmin(admin.ModelAdmin):
        search_fields = ['chofer',]
        list_display = ('chofer','hora_entrada','hora_salida','peso_bruto','peso_tara','peso_neto','peso_despacho','peso_diferencial','peso_porcentaje','activo')
        list_filter = ['chofer','activo']

admin.site.register(romana,romanaadmin)
