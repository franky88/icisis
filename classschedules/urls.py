from django.conf.urls import url, include
from . import views

app_name = 'schedule'
urlpatterns = [
	url(r'^$', views.scheduleIndex, name="scheduleindex"),
	url(r'^(?P<pk>[0-9]+)/$', views.scheduleDetail, name='detail'),
	url(r'^editschedule/(?P<pk>[0-9]+)/$', views.editSchedule, name='edit'),
	url(r'^addschedule/$', views.addSchedule, name="addschedule"),
]