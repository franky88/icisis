from django.contrib import admin
from .models import Student, StudentInfo, Gender
# Register your models here.
class StudentInfoInline(admin.StackedInline):
	model = StudentInfo
	extra = 0

class StudentInfoAdmin(admin.ModelAdmin):
	list_display = ['student', 'address', 'father_name', 'mother_name', 'timestamp', 'date_updated']
	search_fields = ['student']
	list_filter = ['timestamp']

class StudentAdmin(admin.ModelAdmin):
	list_display = ['full_name', 'lrn_or_id_number', 'birth_day', 'gender', 'department', 'course', 'timestamp', 'date_updated']
	list_filter = ['timestamp', 'date_updated']
	search_fields = ['lrn_or_id_number', 'last_name', 'first_name']
	inlines = [StudentInfoInline]




admin.site.register(Student, StudentAdmin)
admin.site.register(StudentInfo, StudentInfoAdmin)
admin.site.register(Gender)