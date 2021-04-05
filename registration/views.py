from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import RegistrationForm
from . models import Registration, ApprovedRegistrations
from courses.models import Course


#decorators for protected views
from resultportal.decorators import student_required, userprofile_student_required, first_login_password_changed
# login url
from resultportal.settings import student_login_url

# view to create new registrations
@userprofile_student_required
@first_login_password_changed
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
                    approved = False
                    try:
                        ApprovedRegistrations.objects.get(rollnum=student.rollnum, semester=student.semester)
                        approved = True
                    except:
                        approved = False
                    new_registration = Registration(student_id = student, course_id = course, is_approved = approved)
                    new_registration.save()

    else:
        form = RegistrationForm(request=request)

    context = {
        'RegistrationForm': form
    }

    return render(request, 'registration/CreateRegistration.html', context)

@userprofile_student_required
@first_login_password_changed
@student_required(login_url=student_login_url, redirect_field_name='')
def UpdateRegStatus(request):
    student  = request.user.userprofilestudent
    rollnum  = student.rollnum
    semester = student.semester
    try:
        ApprovedRegistrations.objects.get(rollnum=rollnum, semester=semester)
        reg = Registration.objects.filter(student_id=request.user.userprofilestudent)

        for r in reg:
            r.is_approved = True
            r.save()
    except:
        messages.error(request, "No updates", extra_tags="reg-update")
    
    return redirect('student:RegistrationStatus')




