from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required #Remover al eliminar todos
from .models import chofer, romana
from django.views.generic import ListView, TemplateView

class home(TemplateView):
	template_name = 'romana/home.html'

class Choferes(ListView):
	# filter(usuario = self.request.user) 
	template_name = 'romana/choferes_list.html'
	model = chofer
	context_object_name = 'choferes'
	paginate_by = 10

class Romana(ListView):
	# filter(usuario = self.request.user) 
	template_name = 'romana/romana_list.html'
	model = romana
	context_object_name = 'romanas'
	paginate_by = 10
