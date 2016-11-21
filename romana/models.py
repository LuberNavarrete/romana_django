from django.db import models
from django.contrib.auth.models import User

tpodoc = (
    ('E', 'Entrada'),
    ('S', 'Salida'),
)

class chofer(models.Model):
	ci = models.IntegerField()
	nombre = models.CharField(max_length=100)
	placa_vehiculo = models.CharField(max_length=20)
	usuario = models.ForeignKey(User)
	# creado = models.DateTimeField(auto_now_add = True, editable=False)
	modificado = models.DateTimeField(auto_now = True, editable=False)
	observacion = models.TextField(max_length=200, blank = True)
	activo = models.BooleanField(default = 'true')
	
	def __str__(self):
		return self.nombre

class empresa(models.Model):
    rif = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    # usuario = models.ForeignKey(User)
    creado = models.DateTimeField(auto_now_add = True, editable=False)
    modificado = models.DateTimeField(auto_now = True, editable=False)
    observacion = models.TextField(max_length=200, blank = True)
    activo = models.BooleanField(default = 'true')
    
    def __str__(self):
		return self.nombre

class romana(models.Model):
	empresa = models.ForeignKey(empresa,limit_choices_to={'activo': True})
	chofer = models.ForeignKey(chofer,limit_choices_to={'activo': True})
	hora_entrada = models.DateTimeField(null = True)
	hora_salida = models.DateTimeField(null = True)
	tipo_de_documento = models.CharField(choices = tpodoc, max_length=10, default = 'E')
	de = models.CharField(max_length=100, blank = True)
	hasta = models.CharField(max_length=100, blank = True)
	# guia = models.CharField(max_length=50)
	peso_bruto = models.FloatField(default = 0)
	peso_tara = models.FloatField(default = 0)
	peso_neto = models.FloatField(editable = False, default = 0)
	# usuario = models.ForeignKey(User)
	peso_despacho = models.FloatField(default = 0)
	peso_diferencial = models.FloatField(editable = False, default = 0)
	peso_porcentaje = models.FloatField(editable = False, default = 0)
	creado = models.DateTimeField(auto_now_add = True, editable=False)
	modificado = models.DateTimeField(auto_now = True, editable=False)
	observacion = models.TextField(max_length=200, blank = True)
	activo = models.BooleanField(default = 'true')

	def save(self, *args, **kwargs):
		self.peso_neto = self.peso_bruto - self.peso_tara
		self.peso_diferencial = self.peso_neto - self.peso_despacho
		self.peso_porcentaje = (self.peso_neto - self.peso_despacho) * 100 / self.peso_neto

		super(romana, self).save(*args, **kwargs)

	def __str__(self):
		return self.tipo_de_documento
