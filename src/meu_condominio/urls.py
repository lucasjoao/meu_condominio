from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='mc-index'),
	url(r'^login/$', views.login, name='mc-login'),
	url(r'^signup/$', views.signup, name='mc-signup'),
	url(r'^update/$', views.update, name='mc-update'),
	url(r'^home/$', views.home, name='mc-home'),
  url(r'^logout/$', views.logout_view, name='mc-logout'),
  url(r'^financas/$', views.financas, name='mc-financas'),
  url(r'^espacos/$', views.espacos, name='mc-espacos'),
  url(r'^funcionarios/$', views.funcionarios, name='mc-funcionarios'),
  url(r'^funcionarios/f_add$', views.f_add, name='mc-f_add'),
]
