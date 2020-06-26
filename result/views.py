from django.shortcuts import render
from . forms import ResultForm
from . models import Result
from users.models import UserProfileStudent
from courses.models import Course
from resultportal.decorators import instructor_required
from django.http import JsonResponse
from django.contrib import messages
from registration.models import Registration

# openpyxl module
import openpyxl

# create a result 
# access restricted to faculty
@instructor_required(login_url='account_login')
def CreateResult(request):
    if request.method == "POST":
        excel_file = request.FILES["excel_file"]
        form = ResultForm(request.POST, request=request)

        if form.is_valid():
            wb = openpyxl.load_workbook(excel_file)
            worksheet = wb["Sheet1"]

            form_input = form.cleaned_data

            for row in worksheet.iter_rows():
                row_data = list()
                for cell in row:
                    row_data.append(str(cell.value))

                try:
                    user_inst = UserProfileStudent.objects.get(rollnum=row_data[0])
                except:
                    user_inst = None
                course_inst = Course.objects.get(cid=form_input.get('course'))
    
                if user_inst != None:
                    try:
                        user_reg = Registration.objects.get(student_id=user_inst, course_id=course_inst)
                    except:
                        user_reg = None
                    if user_reg != None and user_reg.is_approved == True:
                        Result.objects.create(
                            student = user_inst,
                            course  = course_inst,
                            course_name = course_inst.name,
                            exam_type = form_input.get('exam_type'),
                            student_marks = row_data[1],
                            total_marks = form_input.get('total_marks'),
                            highest_marks = form_input.get('highest_marks'),
                            avg_marks = form_input.get('avg_marks')
                        )
            messages.info(request, "Results sent Successfully", extra_tags="result-success")

    else:
        form = ResultForm(request=request)

    context = {
        'form': form
    }

    return render(request, 'result/CreateResult.html', context)

#get course name from course id via ajax request
def GetCourseName(request):
    cid = request.GET.get('cid', None)
    course = Course.objects.get(pk=cid)
    cname =  course.name
    
    data = {'course_name': cname}
    return JsonResponse(data)
