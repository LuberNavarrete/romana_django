from django.contrib import admin
from .models import empresa, chofer, romana

class empresaadmin(admin.ModelAdmin):
	search_fields = ['rif','nombre']
        list_display = ('rif','nombre','modificado','observacion','activo')
        list_filter = ['activo','nombre']

admin.site.register(empresa,empresaadmin)

class choferadmin(admin.ModelAdmin):
        search_fields = ['ci','nombre']
        list_display = ('ci','nombre','placa_vehiculo','modificado','observacion','activo')
        list_filter = ['activo','nombre']

admin.site.register(chofer,choferadmin)

class romanaadmin(admin.ModelAdmin):
        search_fields = ['empresa',]
        list_display = ('empresa','chofer','hora_entrada','hora_salida','peso_bruto','peso_tara','peso_neto','peso_despacho','peso_diferencial','peso_porcentaje','activo')
        list_filter = ['empresa','activo']

admin.site.register(romana,romanaadmin)
