from django import forms
from .models import empresa, romana

class EmpresaForm(forms.ModelForm):
	
	class Meta:
		model = empresa
		fields = ('rif', 'nombre', 'usuario','observacion','activo')