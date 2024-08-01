from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from django.db.models import Q
from django.contrib import messages
from . models import Employer, JobSeeker

# Create your views here.
# User Logout 
def logout(request):
    auth.logout(request)
    return redirect('home')

# Employer Registration
def register_employer(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')

        if password == confirm_password:
            if User.objects.filter(Q(username=username)|Q(email=email)).exists():
                messages.error(request, 'user already exist!')
                return redirect('register_employer')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                company_name = request.POST.get('company_name')
                company_description = request.POST.get('company_description')
                website = request.POST.get('website')
                phone_number = request.POST.get('phone_number')
                location = request.POST.get('location')
                employer = Employer.objects.create(
                    email=email,
                    user=user,
                    company_name=company_name,
                    company_description=company_description,
                    website=website,
                    phone_number=phone_number,
                    location=location
                    )
                employer.save()
                return redirect('home')
        else:
            messages.error(request, 'password error')
            return redirect('register_employer')
    return render(request, 'register_employer.html')

# Jobseeker Registration
def register_jobseeker(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')

        if password == confirm_password:
            if User.objects.filter(Q(username=username)|Q(email=email)).exists():
                messages.error(request, 'user already exist!')
                return redirect('register_jobseeker')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
                user.save()
                phone_number = request.POST.get('phone_number')
                location = request.POST.get('location')
                resume = request.FILES.get('resume')
                jobseeker = JobSeeker.objects.create(user=user, resume=resume, first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, location=location)
                jobseeker.save()
                return redirect('login')
        else:
            messages.error(request, 'password error')
            return redirect('register_jobseeker')
    return render(request, 'register_jobseeker.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            employer_users = User.objects.filter(employer__isnull=False)
            if user in employer_users:
                return redirect('employer_dashboard')
            else:
                return redirect('home')
        else:
            messages.error(request, 'invalid credentials')
            return redirect('login')
    return render(request, 'login.html')

def delete_user(request):
    user = request.user
    logout(request)
    user.delete()
    return redirect('home')