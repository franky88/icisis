from django.conf.urls import include, url
from . import views

app_name = 'main'
urlpatterns = [
    url(r'^$', views.mainLogin, name='mainindex'),
    url(r'^logout/$', views.mainLogout, name='logout'),
]