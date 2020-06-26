from django.contrib import admin
from . models import Registration


class ResgistrationAdmin(admin.ModelAdmin):
    list_display = ('RollNum','student_id', 'course_id', 'Semester', 'is_approved')
    list_editable = ('is_approved',)
    list_filter = ('course_id', 'is_approved', 'student_id__semester')
    search_fields = ('student_id__rollnum', 'student_id__name')
    
    def RollNum(self, obj):
        return(obj.student_id.rollnum)
    
    def Semester(self, obj):
        return(obj.student_id.semester)

admin.site.register(Registration, ResgistrationAdmin)
