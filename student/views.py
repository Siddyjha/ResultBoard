from django.shortcuts import render, redirect
from registration.models import Registration
from result.models import Result
from courses.models import Course
from result.utils import get_sub_grade
#forms
from users.forms import UserProfileForm

from resultportal.settings import student_login_url

# decortors for protected views
from resultportal.decorators import student_required, userprofile_student_required, first_login_password_changed

# student's home view
@userprofile_student_required   
@student_required(login_url=student_login_url, redirect_field_name='')
@first_login_password_changed
def StudentHomeView(request):

    return render(request, 'student/StudentHome.html')

# view for student's to see their registration status
@userprofile_student_required  
@student_required(login_url=student_login_url, redirect_field_name='')
@first_login_password_changed
def RegistrationStatusView(request):
    
    approved_reg_set = Registration.objects.filter(student_id=request.user.userprofilestudent, is_approved=True)
    pending_reg_set = Registration.objects.filter(student_id=request.user.userprofilestudent, is_approved=False)

    context = {
        'approved_reg': approved_reg_set,
        'pending_reg': pending_reg_set
    }

    return render(request, 'student/RegistrationStatus.html', context)

# view all registered courses
@userprofile_student_required  
@student_required(login_url=student_login_url, redirect_field_name='')
@first_login_password_changed
def RegisteredCoursesView(request):

    reg_set = Registration.objects.filter(student_id=request.user.userprofilestudent, is_approved=True)

    context = {
        'reg_courses': reg_set
    }

    return render(request, 'student/RegisteredCourse.html', context)

#view all recent sent results  
@userprofile_student_required
@student_required(login_url=student_login_url, redirect_field_name='')
@first_login_password_changed
def AllResultView(request):

    results = Result.objects.filter(student=request.user.userprofilestudent).order_by('date').reverse()

    context = {
        'result_set': results
    }

    return render(request, 'student/ViewResults.html', context)

# edit userprofile
@userprofile_student_required  
@student_required(login_url=student_login_url, redirect_field_name='')
@first_login_password_changed
def EditUserProfileView(request):

    try:
        current_profile = request.user.userprofilestudent
    except:
        return redirect('users:CreateProfile')

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=current_profile)
        if form.is_valid():
            reg_list = Registration.objects.filter(student_id=current_profile)
            # delete existing registrations
            for reg in reg_list:
                reg.delete()
            form.save()
            
            return redirect('student:ViewResults')

    else:
        form = UserProfileForm(instance=current_profile)

    context = {
        'form': form
    }

    return render(request, 'student/EditProfile.html', context)

# detailed view of course and all it's results
#@userprofile_student_required  
@student_required(login_url=student_login_url, redirect_field_name='')
@first_login_password_changed
def DetailResultView(request, cid):
    
    student = request.user.userprofilestudent
    course  = Course.objects.get(cid=cid)
    
    results = Result.objects.all().filter(student=student, course=course)

    perc=0
    for res in results:
        perc += res.get_contribution()
    
    grade = get_sub_grade(results=results)

    context = {
        'results': results,
        'course': course,
        'grade': grade,
        'perc': perc
    }

    return render(request, 'student/DetailResult.html', context)
