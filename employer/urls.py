from . import views
from django.urls import path

urlpatterns = [
    path('dashboard/', views.employer_dashboard, name='employer_dashboard'),
    path('edit-company-details/', views.edit_company_details, name='edit_company_details'),
    path('post-new-job/', views.post_new_job ,name='post_new_job'),
    path('jobs-posted/', views.jobs_posted, name='jobs_posted'),
    path('delete-job/<int:id>/', views.delete_job, name='delete_job'),
    path('edit-job/<int:id>/', views.edit_job, name='edit_job'),
    path('job-applications-recieved', views.job_applications_recieved, name='job_applications_recieved'),
    path('change-application-status/<int:id>/', views.update_application_status, name='update_application_status'),
    path('delete-application/<int:id>/', views.delete_application, name='delete_application'),
]