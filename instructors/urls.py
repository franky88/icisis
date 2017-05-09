from django.conf.urls import url, include
from . import views

app_name = 'instructor'
urlpatterns = [
	url(r'^$', views.instructorIndex, name="instructorindex"),
	url(r'^(?P<pk>[0-9]+)/$', views.instructorDetail, name='detail'),
	url(r'^(?P<pk>[0-9]+)/edit$', views.editInstructor, name='edit'),
	url(r'^addinstructor$', views.addInstructor, name="addinstructor"),
]