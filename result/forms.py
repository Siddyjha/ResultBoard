from django import forms
from courses.models import Course

class ResultForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ResultForm, self).__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.filter(instructor=self.request.user.userprofilefaculty)

    course = forms.ModelChoiceField(queryset=None)
    course_name = forms.CharField(max_length=254)
    exam_type = forms.CharField(max_length=254)
    total_marks = forms.IntegerField()
    highest_marks = forms.IntegerField()
    avg_marks = forms.IntegerField()
    

    
