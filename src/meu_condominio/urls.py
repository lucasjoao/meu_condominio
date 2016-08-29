from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='mc-index'),
	url(r'^login/$', views.login, name='mc-login'),
	url(r'^signup/$', views.signup, name='mc-signup'),
]
