from django.contrib import admin
from django.shortcuts import render
from django.conf.urls import url
from django.urls import path
from . models import Registration
from . models import ApprovedRegistrations
import openpyxl

class ResgistrationAdmin(admin.ModelAdmin):
    list_display = ('RollNum','student_id', 'course_id', 'Semester', 'is_approved')
    list_editable = ('is_approved',)
    list_filter = ('course_id', 'is_approved', 'student_id__semester')
    search_fields = ('student_id__rollnum', 'student_id__name')

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            url('BulkRegApproval/', self.admin_site.admin_view(self.CreateReg), name="BulkReg")
        ]
        return my_urls + urls
    
    def RollNum(self, obj):
        return(obj.student_id.rollnum)
    
    def Semester(self, obj):
        return(obj.student_id.semester)

    def CreateReg(self, request):
        if request.method == "POST":
            excel_file = request.FILES["excel_file"]
            wb = openpyxl.load_workbook(excel_file)
            worksheet = wb["Sheet1"]

            for row in worksheet.iter_rows():
                row_data = list()
                for cell in row:
                    row_data.append(str(cell.value))
                
                rollnum = row_data[0]
                ApprovedRegistrations.objects.create(rollnum=rollnum)
        
        return render(request, 'registration/BulkReg.html')

admin.site.register(Registration, ResgistrationAdmin)
admin.site.register(ApprovedRegistrations)
    

    

