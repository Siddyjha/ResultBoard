from django.shortcuts import render
from . models import ResultHistory
from users.models import UserProfileFaculty
from django.http import JsonResponse
from message.utils import Inbox
import json
import openpyxl

# decorators
from resultportal.decorators import instructor_required

# Home view
@instructor_required(login_url='account_login')
def HomeView(request):
    return render(request, 'instructor/Home.html')

@instructor_required
def SentResultView(request):
    ins = request.user.userprofilefaculty
    prev_results = ResultHistory.objects.filter(instructor=ins)
    
    context = {
        'prev_results':prev_results
    }
    return render(request, 'instructor/ResultHistory.html', context)

# Result Preview
class PreviewModel():
    def __init__(self, rollnum, marks):
        self.rollnum = rollnum
        self.marks = marks

#ajax request for result preview
def ResultPreview(request):
    id = request.GET.get('id', None)
    ins = ResultHistory.objects.get(pk=id)
    excel_file = ins.excel_file

    desc = {
        'exam_type': ins.exam_type,
        'created_on': ins.get_date()
    }

    wb = openpyxl.load_workbook(excel_file)
    worksheet = wb["Sheet1"]

    obj_list = list()

    for row in worksheet.iter_rows():
        row_data = list()
        for cell in row:
            row_data.append(str(cell.value))
        obj = PreviewModel(row_data[0], row_data[1])
        obj_list.append(obj)

    json_obj = json.dumps([ob.__dict__ for ob in obj_list])
    data = {
        'desc': desc,
        'json': json_obj
    }
    return JsonResponse(data, safe=False)

# inbox
def InstructorInboxView(request):
    messages = Inbox(request.user).get_messages()

    context = {
        'msg': messages
    }

    return render(request, 'instructor/Inbox.html', context)

    