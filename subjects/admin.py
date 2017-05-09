from django.contrib import admin
from .models import Subject
# Register your models here.

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['descriptive_title', 'subject_code']
    search_fields = ['descriptive_title', 'subject_code']
    list_filter = ['descriptive_title', 'subject_code']



admin.site.register(Subject, SubjectAdmin)
