# bikeProject/urls.py

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^getRotationCount/$', views.getRotationCount, name='getRotationCount'),
    url(r'^login/$', views.Login),
    url(r'^logout/$', views.Logout),
    url(r'^home/$', views.Home),
    url(r'^blog/$', views.Blog),
]