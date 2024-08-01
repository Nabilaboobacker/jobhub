from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/employer-details/', views.employer_details, name='employer_details'),
    path('delete-company/<int:id>/', views.delete_company, name='delete_company'),
    path('dashboard/jobseeker-details/', views.jobseeker_details, name='jobseeker_details'),
]
