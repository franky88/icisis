from django.conf.urls import url
from . import views

app_name = "bulletin"
urlpatterns = [
    url(r'^$', views.bulletinIndex, name='bulletinindex'),
]