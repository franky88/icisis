from django.db import models
from django.db.models import F, FloatField, Sum
from subjects.models import Subject
from instructors.models import Instructor
from students.models import Student
from main.models import Course

# Create your models here.
class Block(models.Model):
	block_name = models.CharField(max_length=120)
	course = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)
	def __str__(self):
		return self.block_name

class Schedule(models.Model):
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default=1)
	teacher = models.ForeignKey(Instructor, on_delete=models.CASCADE, default=1)
	block = models.ForeignKey(Block, on_delete=models.CASCADE, default=1)
	student = models.ManyToManyField(Student)
	date_start = models.DateField()
	end_date = models.DateField()
	time_start = models.TimeField()
	time_end = models.TimeField()
	total_number_of_modules = models.IntegerField(default=8)
	# def total_subject_fee(self):
	# 	Subject.objects.all().aggregate(subjectfee = Sum(F('subject_fee')/F("8"), output_field=FloatField()))
	# 	return subjectfee

	def get_students(self):
		return "\n".join([s.full_name() for s in self.student.all()])

	def subject_date(self):
		subjectdate = "%s-%s"%(self.date_start, self.end_date)
		return subjectdate

	def subject_time(self):
		subjecttime = "%s-%s"%(self.time_start, self.time_end)
		return subjecttime
		
	def __str__(self):
		return "(%s to %s) - %s"%(self.subject_date(), self.subject_time(), self.subject.descriptive_title)


	
