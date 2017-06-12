from django.db import models
from main.models import SchoolYear, Semester
from instructors.models import Instructor
# Create your models here.
class Subject(models.Model):
	subject_code = models.CharField(max_length=20, unique=True)
	descriptive_title = models.CharField(max_length=120, unique=True)
	units = models.IntegerField(default=3)
	hours = models.IntegerField(default=80)
	subject_fee = models.FloatField()
	def __str__(self):
		return self.descriptive_title

