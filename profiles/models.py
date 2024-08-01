from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class JobCategory(models.Model):
    job_category = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.job_category

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200, unique=True)
    company_description = models.TextField()
    website = models.URLField(max_length=200, unique=True, blank=True)
    email = models.EmailField(max_length=200, unique=True)
    phone_number = models.CharField(max_length=13)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name
    
class JobSeeker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    category = models.ForeignKey(JobCategory, on_delete=models.SET_NULL, null=True, blank=True)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    phone_number = models.CharField(max_length=13)
    location = models.CharField(max_length=100)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    skills = models.CharField(max_length=400, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name
    
    
class Job(models.Model):
    title = models.CharField(max_length=350)
    description = models.TextField()
    category = models.ForeignKey(JobCategory, on_delete=models.SET_NULL, null=True, blank=True)
    company = models.ForeignKey(Employer, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    job_type = models.CharField(max_length=100)
    experience = models.CharField(max_length=20)
    is_featured = models.BooleanField(default=False)
    salary = models.CharField(max_length=15, blank=True)
    qualification = models.CharField(max_length=200)
    skills_required = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class JobApplication(models.Model):
    PENDING = 'Pending'
    NOT_SELECTED = 'Not Selected'
    UNDER_REVIEW = 'Under Review'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (NOT_SELECTED, 'Not Selected'),
        (UNDER_REVIEW, 'Under Review'),
    ]

    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    jobseeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=PENDING, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
      
    def __str__(self):
        return self.user.first_name
    
