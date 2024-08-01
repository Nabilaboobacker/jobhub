from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('register/employer/', views.register_employer, name='register_employer'),
    path('register/jobseeker/', views.register_jobseeker, name='register_jobseeker'),
    path('delete_user/', views.delete_user, name='delete_user'),
]
