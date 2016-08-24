from django.contrib import admin
from .models import empresa, chofer, romana

class empresaadmin(admin.ModelAdmin):
	search_fields = ['rif','nombre']
        list_display = ('rif','nombre','usuario','creado','modificado','observacion','activo')
        list_filter = ['activo','nombre']

admin.site.register(empresa,empresaadmin)

class choferadmin(admin.ModelAdmin):
        search_fields = ['ci','nombre']
        list_display = ('ci','nombre','placa_vehiculo','usuario','creado','modificado','observacion','activo')
        list_filter = ['activo','nombre']

admin.site.register(chofer,choferadmin)

class romanaadmin(admin.ModelAdmin):
        search_fields = ['empresa','guia','hora_entrada','hora_salida']
        list_display = ('empresa','chofer','hora_entrada','hora_salida','guia','peso_tara','peso_neto','usuario','creado','modificado','observacion','activo')
        list_filter = ['empresa','guia','hora_entrada','hora_salida']

admin.site.register(romana,romanaadmin)
