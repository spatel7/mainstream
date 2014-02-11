from django.conf.urls import patterns, url
from mainstream import views

urlpatterns = patterns('',
			url(r'^$', views.index, name='index'))