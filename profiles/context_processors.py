from django.contrib.auth.models import User

def employer_users(request):
    employer_users = User.objects.filter(employer__isnull=False)
    context = {'employer_users':employer_users}
    return context
