from django.conf.urls import url 
from . import views 
urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^login$', views.login),
    url(r'^dashboard$', views.dashboard),
    url(r'^(?P<name>[\w ]+)/show$', views.show),
    url(r'^(?P<name>[\w ]+)/add$', views.add),
    url(r'^(?P<name>[\w ]+)/remove$', views.remove),
    url(r'^logout$', views.logout),
    ]