from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from profiles.models import Job, JobSeeker, JobApplication
from django.db.models import Q

# Home view
def home(request):
    # Get all users who are employers
    employer_users = User.objects.filter(employer__isnull=False)

    if request.user.is_authenticated:
        if request.user.is_superuser:
            # Redirect superusers to employer details page
            return redirect('employer_details')
        elif request.user in employer_users:
            # Redirect employers to their dashboard
            return redirect('employer_dashboard')
        elif request.user not in employer_users:
            # Handle jobseeker view
            user_details = get_object_or_404(JobSeeker, user=request.user)
            # Get featured jobs matching user's category
            featured_jobs = Job.objects.filter(is_featured=True, category=user_details.category)
            # Get IDs of jobs the user has already applied to
            user_job_applications = JobApplication.objects.filter(user=request.user).values_list('job_id', flat=True)
            # Get all jobs in user's category for job feed
            job_feed = Job.objects.filter(category=user_details.category)
            context = {
                'featured_jobs': featured_jobs,
                'job_feed': job_feed,
                'user_job_applications': user_job_applications,
            }
    else:
        # For non-authenticated users, show all featured jobs
        featured_jobs = Job.objects.filter(is_featured=True)
        context = {'featured_jobs': featured_jobs}
    
    return render(request, 'home.html', context)

# View for role selection page
def role_selection(request):
    return render(request, 'role_selection.html')

# Job search functionality
def job_search(request):
    context = {}
    user_job_applications = []

    if request.method == 'POST':
        search_keyword = request.POST.get('search_keyword')
        if search_keyword:
            # Perform job search across multiple fields
            jobs = Job.objects.filter(
                Q(title__icontains=search_keyword) |
                Q(description__icontains=search_keyword) |
                Q(company__company_name__icontains=search_keyword) |
                Q(location__icontains=search_keyword) |
                Q(qualification__icontains=search_keyword) |
                Q(skills_required__icontains=search_keyword) |
                Q(category__job_category__icontains=search_keyword)
            )

            if jobs:
                if request.user.is_authenticated:
                    # Get IDs of jobs the user has already applied to
                    user_job_applications = JobApplication.objects.filter(user=request.user).values_list('job_id', flat=True)
                
                context = {
                    'jobs': jobs,
                    'search_keyword': search_keyword,
                    'user_job_applications': user_job_applications,
                }
        else:
            # If no search keyword, redirect to home
            return redirect('home')
    
    return render(request, 'job_search.html', context)