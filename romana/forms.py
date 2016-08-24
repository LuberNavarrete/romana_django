from django import forms
from .models import empresa, romana

class EmpresaForm(forms.ModelForm):
	
	class Meta:
		model = empresa
		fields = ('rif', 'nombre', 'usuario','observacion','activo')

class RomanaForm(forms.ModelForm):
	
	class Meta:
		model = romana
		fields = ('empresa', 'chofer', 'hora_entrada','hora_salida','guia','peso_tara','peso_neto','observacion','activo')
