from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('role_selection/', views.role_selection, name='role_selection'),
    path('job-search', views.job_search, name='job_search'),
]