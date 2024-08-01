from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from profiles.models import Employer, JobSeeker

# Create your views here.

def employer_details(request):
    employer_users = Employer.objects.all()
    context = {'employer_users': employer_users,}
    return render(request, 'manager/employer_details.html', context)

def delete_company(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect('home')

def jobseeker_details(request):
    jobseekers = JobSeeker.objects.all()
    context = {'jobseekers':jobseekers}
    return render(request, 'manager/jobseeker_details.html', context)