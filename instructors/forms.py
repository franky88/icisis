from django import forms
from .models import Instructor

class InstructorForm(forms.ModelForm):
	class Meta:
		model = Instructor
		fields = [
			"id_number",
			"first_name",
			"middle_name",
			"last_name",
			"extension_name",
			"gender",
			"birth_date",
			"email_add",
			"contact_number",
			"employment_status",
			"adddress",
			"department",
			"image",
		]