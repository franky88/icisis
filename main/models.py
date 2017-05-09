from django.db import models
# Create your models here.
class SideNav(models.Model):
	class Meta:
		ordering = ["app_name"]
	app_name = models.CharField(max_length=60, unique=True)

	def link_to_display(self):
		link = "%s:%sindex"%(self.name)
		return link

	def __str__(self):
		return self.link_to_display()


class SchoolYear(models.Model):
	start_year = models.CharField(max_length=4)
	end_year = models.CharField(max_length=4)
	def school_year(self):
		schoolyear = "%s - %s"%(self.start_year, self.end_year)
		return schoolyear

	def __str__(self):
		return self.school_year()

class Semister(models.Model):
	schoolyear = models.ForeignKey(SchoolYear, on_delete=models.CASCADE)
	sems = (
			("First Semester", "1st Sem"),
			("Second Semister", "2nd Sem"),
		)
	semister = models.CharField(max_length=15, choices=sems)
	start_date = models.DateField()
	end_date = models.DateField()
	def semister_range(self):
		semrange = "%s - %s"%(self.start_date, self.end_date)
		return semrange

	def __str__(self):
		return self.semister

class Department(models.Model):
	department = models.CharField(max_length=120)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	def __str__(self):
		return self.department

class Track(models.Model):
	schoolyear = models.ForeignKey(SchoolYear, on_delete=models.CASCADE)
	TRACKS = (
			("Humanities","HUMMS"),
			("Science","STEM"),
			("Arts and Design", "ARTS & DESIGN"),
			("Sports", "SPORTS"),
			("Technical Vocational", "TVL"),
		)
	track = models.CharField(max_length=22, choices=TRACKS)
	def __str__(self):
		return self.track

class Strand(models.Model):
	track = models.ForeignKey(Track, on_delete=models.CASCADE)
	strand = models.CharField(max_length=60, default="ICT")
	def __str__(self):
		return self.strand

class Course(models.Model):
	semister = models.ForeignKey(Semister, on_delete=models.CASCADE)
	department = models.ForeignKey(Department, on_delete=models.CASCADE)
	course_title = models.CharField(max_length=255)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	def __str__(self):
		return self.course_title
	
