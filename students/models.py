from django.db import models
from main.models import Department, Course



# Create your models here.
def upload_location(instance, filename):
	location = "%s/%s"%(instance.id, filename)
	return location

class Student(models.Model):
	lrn_or_id_number = models.CharField(max_length=20, unique=True)
	first_name = models.CharField(max_length=60)
	middle_name = models.CharField(max_length=60)
	last_name = models.CharField(max_length=60)
	extension_name = models.CharField(max_length=5, blank=True)
	department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
	course = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)
	birth_day = models.DateField()
	image = models.ImageField(upload_to=upload_location,
		height_field="height_field",
		width_field="width_field",
		blank=True,
		null=True,
		)
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	def full_name(self):
		fullname = '%s %s %s %s'%(self.first_name, self.middle_name, self.last_name, self.extension_name)
		return fullname

	def __str__(self):
		return self.full_name()

class StudentInfo(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	address = models.TextField()
	SEX = (
			('Male', 'Male'),
			('Female', 'Female'),
		)
	gender = models.CharField(max_length=6, choices=SEX)
	father_name = models.CharField(max_length=120, verbose_name="Father's full name")
	mother_name = models.CharField(max_length=120, verbose_name="Mother's maiden name")
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	def __str__(self):
		return self.student.full_name()