from django.urls import path
from . import views

urlpatterns = [
    path('jobseeker-dashboard', views.jobseeker_dashboard, name='jobseeker_dashboard'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('applied-jobs/', views.applied_jobs, name='applied_jobs'),
    path('apply-now/<int:id>/', views.apply_now, name='apply_now'),
]