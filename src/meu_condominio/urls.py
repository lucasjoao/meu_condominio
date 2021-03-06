from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='mc-index'),
	url(r'^login/$', views.login, name='mc-login'),
	url(r'^signup/$', views.signup, name='mc-signup'),
	url(r'^update/(?P<id>\d+)/$', views.update, name='mc-update'),
	url(r'^home/$', views.home, name='mc-home'),
  url(r'^logout/$', views.logout_view, name='mc-logout'),
  url(r'^financas/$', views.financas, name='mc-financas'),
  url(r'^financas/fin_add$', views.fin_add, name='mc-fin_add'),
  url(r'^financas/fin_view$', views.fin_view, name='mc-fin_view'),
  url(r'^financas/fin_edit/(?P<id>\d+)/$', views.fin_edit, name='mc-fin_edit'),
  url(r'^financas/fin_view_relatorio/(?P<id>\d+)/$',
    views.fin_view_relatorio, name='mc-fin_view_relatorio'),
  url(r'^espacos/$', views.espacos, name='mc-espacos'),
  url(r'^espacos/esp_res$', views.esp_res, name='mc-e_res'),
  url(r'^espacos/esp_view$', views.esp_view, name='mc-e_view'),
  url(r'^espacos/esp_del/(?P<id>\d+)/$', views.esp_del, name='mc-e_del'),
  url(r'^funcionarios/$', views.funcionarios, name='mc-funcionarios'),
  url(r'^funcionarios/f_add$', views.f_add, name='mc-f_add'),
  url(r'^funcionarios/f_view$', views.f_view, name='mc-f_view'),
  url(r'^funcionarios/f_del/(?P<id>\d+)/$', views.f_del, name='mc-f_del'),
  url(r'^funcionarios/f_edit/(?P<id>\d+)/$', views.f_edit, name='mc-f_edit'),
  url(r'^moradores/$', views.moradores, name='mc-moradores'),
  url(r'^moradores/m_add$', views.m_add, name='mc-m_add'),
  url(r'^moradores/m_view$', views.m_view, name='mc-m_view'),
  url(r'^moradores/m_del/(?P<id>\d+)/$', views.m_del, name='mc-m_del'),
  url(r'^moradores/m_edit/(?P<id>\d+)/$', views.m_edit, name='mc-m_edit'),
]
