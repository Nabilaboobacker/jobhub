from django import forms
from profiles . models import Employer, Job, JobApplication


class EditEmployerDetailsForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ('company_name', 'company_description', 'website', 'email', 'phone_number', 'location')


class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('title', 'description', 'location', 'job_type', 'experience', 'is_featured', 'salary', 'qualification', 'skills_required')


class EditJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('title', 'description', 'location', 'job_type', 'experience', 'is_featured', 'salary', 'qualification', 'skills_required')
        

class EditApplicationStatusForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ('status',)




