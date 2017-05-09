from django.contrib import admin
from .models import SchoolYear, Semister, Track, Strand, Department, Course, SideNav
# Register your models here.




admin.site.register(SideNav)
admin.site.register(SchoolYear)
admin.site.register(Semister)
admin.site.register(Track)
admin.site.register(Strand)
admin.site.register(Department)
admin.site.register(Course)