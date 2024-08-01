from profiles.models import JobSeeker
from django import forms


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = JobSeeker
        fields = ('email', 'phone_number', 'location', 'resume', 'skills')