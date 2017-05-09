from django import forms
from .models import Subject

class SubjectForm(forms.ModelForm):
	class Meta:
		model = Subject
		fields = [
			'subject_code',
			'descriptive_title',
			'subject_fee',
		]