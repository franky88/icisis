from django.contrib import admin
from .models import SchoolYear, Semester, Track, Strand, Department, Course, SideNav
# Register your models here.




admin.site.register(SideNav)
admin.site.register(SchoolYear)
admin.site.register(Semester)
admin.site.register(Track)
admin.site.register(Strand)
admin.site.register(Department)
admin.site.register(Course)