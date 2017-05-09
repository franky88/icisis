from django.conf.urls import url, include
from . import views

app_name = 'subject'
urlpatterns = [
	url(r'^$', views.subjectIndex, name="subjectindex"),
	url(r'^(?P<pk>[0-9]+)/$', views.subjectDetail, name="detail"),
	url(r'^addsubject/$', views.addSubject, name="addsubject"),
	url(r'^editsubject/(?P<pk>[0-9]+)/$', views.editSubject, name='edit'),
]