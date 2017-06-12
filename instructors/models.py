from django.db import models
from main.models import Department
from students.models import Student

# Create your models here.
class EmploymentStatus(models.Model):
	status = models.CharField(max_length=120)
	def __str__(self):
		return self.status

def upload_location(instance, filename):
	location = "%s/%s"%(instance.id, filename)
	return location
class Instructor(models.Model):
	first_name = models.CharField(max_length=60)
	middle_name = models.CharField(max_length=60)
	last_name = models.CharField(max_length=60)
	extension_name = models.CharField(max_length=5, null=True, blank=True)
	sex = (
			("MALE", "MALE"),
			("FEMALE", "FEMALE"),
		)
	gender = models.CharField(max_length=6, choices=sex)
	birth_date = models.DateField()
	email_add = models.EmailField()
	contact_number = models.CharField(max_length=15)
	adddress = models.TextField()
	employment_status = models.ForeignKey(EmploymentStatus, on_delete=models.CASCADE, default=1)
	department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
	image = models.ImageField(
		upload_to=upload_location, 
		null=True, 
		blank=True
		)
	date_registered = models.DateTimeField(auto_now=False, auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	def full_name(self):
		fullname = "%s %s. %s %s"%(
			self.first_name, 
			self.middle_name[0], 
			self.last_name, 
			self.extension_name
			)
		return fullname

	def id_number(self):
		idnumber = "%s%s%s%s%s2017"%(self.first_name[0], self.middle_name[0], self.last_name[0], self.extension_name, self.id)
		return idnumber

	def __str__(self):
		return self.full_name()