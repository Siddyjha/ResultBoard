from django.shortcuts import render, redirect
from . forms import RegistrationForm
from . models import Registration
from courses.models import Course
from django.contrib import messages

#decorators for protected views
from resultportal.decorators import student_required, userprofile_student_required
# login url
from resultportal.settings import student_login_url

# view to create new registrations
@userprofile_student_required
@student_required(login_url=student_login_url, redirect_field_name='')
def CreateRegistrationView(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request=request)
        if form.is_valid():
            # create registration for every selected course
            data = form.cleaned_data
            course_list = data.get('courses')
            student = request.user.userprofilestudent

            for x in course_list:
                course = Course.objects.get(cid=x)
                # check if registration already exists
                if Registration.objects.filter(student_id=student, course_id=course).exists():
                    messages.error(request, x, extra_tags="reg-exists")
                else:
                    messages.error(request, x, extra_tags="reg-success")
                    new_registration = Registration(student_id = student, course_id = course, is_approved = False)
                    new_registration.save()

    else:
        form = RegistrationForm(request=request)

    context = {
        'RegistrationForm': form
    }

    return render(request, 'registration/CreateRegistration.html', context)



