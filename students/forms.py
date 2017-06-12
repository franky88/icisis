from django import forms
from .models import Student, StudentInfo

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ['lrn_or_id_number', 
			'first_name', 
			'last_name', 
			'middle_name', 
			'extension_name',
			'gender',
			'department',
			'course',
			'birth_day',
			'image',
			]

class StudentInfoForm(forms.ModelForm):
	class Meta:
		model = StudentInfo
		fields = [
			'student',
			'address',
			'father_name',
			'mother_name',
		]