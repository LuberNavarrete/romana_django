from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required #Remover al eliminar todos
from .forms import EmpresaForm
from .models import empresa, chofer, romana
from django.views.generic import ListView, TemplateView

class home(TemplateView):
	template_name = 'romana/home.html'
	
@login_required
def empresa_add(request):
	form = EmpresaForm()
	return render(request, 'romana/empresas.html',{'form': form})

# @login_required
# def romana_add(request):
	# form = RomanaForm()
	# return render(request, 'romana/romana.html',{'form': form})

class Empresas(ListView):
	# filter(usuario = self.request.user) 
	template_name = 'romana/empresas_list.html'
	model = empresa
	context_object_name = 'empresas'
	paginate_by = 10

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
