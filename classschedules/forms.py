from django import forms
from .models import Schedule, Block

class ScheduleForm(forms.ModelForm):
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
