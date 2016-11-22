from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'^login/$', 'django.contrib.auth.views.login', name = 'login'),
	url(r'^logout/$', 'django.contrib.auth.views.logout', name = 'logout'),
	url(r'^logout-then-login/$', 'django.contrib.auth.views.logout_then_login', name = 'logout_then_login'),
	# url(r'^password-change/$', 'django.contrib.auth.views.password_change', name = 'password_change'),
	# url(r'^password-change/done/$', 'django.contrib.auth.views.password_change_done', name = 'password_change_done'),
	# Index
	url(r'^$', login_required(views.home.as_view()), name = 'home'),
	# CreateViews
	# url(r'^empresasagregar$', views.empresa_add, name = 'empresas_add'),
	# url(r'^romanaagregar$', views.romana_add, name = 'romana_add'),
	# ListViews
	# url(r'^empresas/$', login_required(views.Empresas.as_view()), name = 'empresa_list'),
	url(r'^choferes/$', login_required(views.Choferes.as_view()), name = 'chofer_list'),
	url(r'^romana/$', login_required(views.Romana.as_view()), name = 'romana_list'),
]
