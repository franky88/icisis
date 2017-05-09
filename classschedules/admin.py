from django.contrib import admin
from .models import Schedule, Block
from students.models import Student
from django import forms
from django.contrib.admin.widgets import AdminTimeWidget
# Register your models here.
class MyTimeFormat(forms.ModelForm):
	time_start = forms.TimeField(widget=AdminTimeWidget(format='%H:%M'))
	time_end = forms.TimeField(widget=AdminTimeWidget(format='%H:%M'))
	# student = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=Student.objects.all(), required=True)
	class Meta:
		model = Schedule
		fields = [
			"subject",
			"teacher",
			"student",
			"block",
			"date_start",
			"end_date",
			"time_start",
			"time_end",
		]
	# def __init__(self, *args, **kwargs):
	# 	super(MyTimeFormat, self).__init__(*args, **kwargs)
	# 	self.fields["student"].widget = forms.CheckboxSelectMultiple()
	# 	self.fields["student"].queryset = Student.objects.all()

class MyModelTime(admin.ModelAdmin):
	list_display = ["subject", "teacher", "block", "date_start", "end_date", "time_start", "time_end"]
	list_filter = ["subject", "block", "teacher"]
	search_fields = ["subject", "block", "teacher"]
	form = MyTimeFormat

	def get_students(self, obj):
		return ",\n".join([s.full_name() for s in obj.student.all()])

admin.site.register(Schedule, MyModelTime)
admin.site.register(Block)