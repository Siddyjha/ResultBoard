from django.contrib import admin
from . models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ('cid', 'name')
    search_fields = ('cid',)

admin.site.register(Course, CourseAdmin)