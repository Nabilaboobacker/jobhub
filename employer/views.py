from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, HttpResponseRedirect
from profiles.models import Job, Employer, JobApplication, JobSeeker
from . forms import EditEmployerDetailsForm, AddJobForm, EditJobForm, EditApplicationStatusForm
from django.contrib import messages


# Create your views here.


def postjob(request):
    if request.method == 'POST':
        company = get_object_or_404(Employer, user=request.user)
        title = request.POST.get('title')
        description = request.POST.get('description')
        location = request.POST.get('location')
        job_type = request.POST.get('job_type')
        experience = request.POST.get('experience')
        is_featured = request.POST.get('is_featured')
        salary = request.POST.get('salary')
        qualification = request.POST.get('qualification')
        skills_required = request.POST.get('skills_required')

        if is_featured == 'on':
            is_featured = True
        else:
            is_featured = False

        job = Job.objects.create(title=title,
                                 company = company,
                                 description=description,
                                 location=location,
                                 job_type=job_type,
                                 experience=experience,
                                 is_featured=is_featured,
                                 salary=salary,
                                 qualification=qualification,
                                 skills_required=skills_required
                                 )
        job.save()
    return render(request, 'postjob.html')


def employer_dashboard(request):
    company = get_object_or_404(Employer, user=request.user)
    context = {'company': company}
    return render(request, 'employer dashboard/employer_dashboard.html', context)

def edit_company_details(request):
    company = get_object_or_404(Employer, user=request.user)
    if request.method == 'POST':
        form = EditEmployerDetailsForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            messages.error(request, 'Invalid Details')
    else:
        form = EditEmployerDetailsForm(instance=company)
    context = {'form':form,}

    return render(request, 'employer dashboard/edit_company_details.html', context)

def post_new_job(request):
    if request.method == 'POST':
        company = get_object_or_404(Employer, user=request.user)
        form = AddJobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.company = company
            job.save()
            return redirect('home')
        else:
            messages.error(request, 'invalid form')
    else:
        form=AddJobForm()
    context = {'form':form}
    return render(request, 'employer dashboard/post_new_job.html', context)


def jobs_posted(request):
    company = get_object_or_404(Employer, user=request.user)    
    posted_jobs = Job.objects.filter(company=company)
    context = {'posted_jobs':posted_jobs}
    return render(request, 'employer dashboard/jobs_posted.html', context)

def delete_job(request, id):
    job = get_object_or_404(Job, id=id)
    job.delete()
    return redirect('home')

def edit_job(request, id=1):
    job = get_object_or_404(Job, id=id)
    if request.method == 'POST':
        form = EditJobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, 'Invalid form details')
    else:
        form = EditJobForm(instance=job)
    context = {'form': form,
               'job':job,}
    return render(request, 'employer dashboard/edit_job.html', context)

def job_applications_recieved(request):
    applications_recieved = JobApplication.objects.filter(job__company__user=request.user)
    context = {'applications_recieved':applications_recieved,}
    return render(request, 'employer dashboard/job_applications.html', context)



def update_application_status(request, id):
    application = get_object_or_404(JobApplication, id=id)
    if request.method == 'POST':
        status = request.POST.get('status')
        if status:
            application.status=status
            application.save()
            return redirect('job_applications_recieved')
    return redirect('job_applications_recieved')


def delete_application(request, id):
    job_application = get_object_or_404(JobApplication, id=id)
    job_application.delete()
    return redirect('job_applications_recieved')