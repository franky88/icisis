from django.conf.urls import url, include
from . import views

app_name = 'student'
urlpatterns = [
	url(r'^$', views.studentIndex, name="studentindex"),
	url(r'^(?P<pk>[0-9]+)/$', views.studentDetail, name='detail'),
	url(r'^(?P<pk>[0-9]+)/edit$', views.editStudentInfo, name='editinfo'),
	url(r'^(?P<pk>[0-9]+)/delete$', views.deleteStudent, name='delete'),
	url(r'^editstudent/(?P<pk>[0-9]+)/$', views.editStudent, name='edit'),
	url(r'^addstudent/$', views.addStudent, name="addstudent"),
]
