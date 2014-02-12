from django.conf.urls import patterns, url
from mainstream import views

urlpatterns = patterns('',
			url(r'^$', views.index, name='index'),
			url(r'^add_group/$', views.add_group, name='add_group'),
			url(r'^group/(?P<group_id_url>\w+)/$', views.group, name='group'))