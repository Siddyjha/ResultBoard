from django import forms
from . models import Registration
from courses.models import Course

class RegistrationForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(RegistrationForm, self).__init__(*args, **kwargs)
        # filter queryset on basis of student's semester
        self.fields['courses'].queryset = Course.objects.filter(semester=self.request.user.userprofilestudent.semester)
    
    courses = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=None)
