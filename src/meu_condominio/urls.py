from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='mc-index'),
	url(r'^login/$', views.login, name='mc-login'),
	url(r'^signup/$', views.signup, name='mc-signup'),
	url(r'^(?P<id>[0-9]+)/update/$', views.update, name='mc-update'),
	url(r'^(?P<id>[0-9]+)/home/$', views.home, name='mc-home'),
  url(r'^logout/$', views.logout_view, name='mc-logout'),
]
