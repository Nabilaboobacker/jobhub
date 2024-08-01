from django.shortcuts import render, get_object_or_404, redirect
from profiles.models import JobSeeker, JobApplication, Job
from . forms import EditProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def jobseeker_dashboard(request):
    user_details = get_object_or_404(JobSeeker, user=request.user)
    context = {'user_details': user_details,'applied_jobs':applied_jobs}
    return render(request, 'jobseeker_dashboard/jobseeker_dashboard.html', context)

def edit_profile(request):
    user_details = get_object_or_404(JobSeeker, user=request.user)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=user_details)
        if form.is_valid():
            form.save()
            return redirect('jobseeker_dashboard')
        else:
            messages.error(request, 'invalid form')
    else:
        form = EditProfileForm(instance=user_details)
    context = {'form': form,}
    return render(request, 'jobseeker_dashboard/edit_profile.html', context)

def applied_jobs(request):
    applied_jobs = JobApplication.objects.filter(user=request.user)
    context = {'applied_jobs':applied_jobs,}
    return render(request, 'jobseeker_dashboard/applied_jobs.html', context)


@login_required(login_url='login')
def apply_now(request, id):
    if request.user.is_superuser:
        return redirect('login')
    else:
        job = get_object_or_404(Job, id=id)
        if JobApplication.objects.filter(user=request.user, job=job).exists():
            messages.error(request, 'already_applied')
        else:
            jobseeker = get_object_or_404(JobSeeker, user=request.user)
            application = JobApplication.objects.create(user=request.user, job=job, jobseeker=jobseeker)
            application.save()
            return redirect('home')