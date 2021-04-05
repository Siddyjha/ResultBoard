from django import forms
from .models import UserProfileStudent

class UserProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.label_suffix=""
        self.fields['name'].disabled = True
        self.fields['department'].disabled = True
        self.fields['rollnum'].disabled = True

    class Meta:
        model = UserProfileStudent

        fields = [
            'name',
            'department',
            'rollnum',
            'semester'
        ]

        labels = {
            'name': 'Full Name',
            'department': 'Department',
            'rollnum': 'Your Roll Number',
            'semester': 'semester'
        }