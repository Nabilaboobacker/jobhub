from django.contrib import admin
from . models import Employer, JobSeeker, Job, JobApplication, JobCategory
# Register your models here.

admin.site.register(Employer)
admin.site.register(JobSeeker)
admin.site.register(Job)
admin.site.register(JobApplication) 
admin.site.register(JobCategory)