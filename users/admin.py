from django.contrib import admin
from django.conf.urls import url
from django.shortcuts import render, redirect
from django.contrib.auth.admin import UserAdmin
from . models import User, UserProfileFaculty, UserProfileStudent, DummyModel
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail

import openpyxl

class BulkUserCreate(admin.ModelAdmin):

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            url(r'^CreateUsers/$', self.admin_site.admin_view(self.CreateUsers), name="CreateUser")
        ]
        return my_urls + urls

    def CreateUsers(self, request):
        if request.method == "POST":
            excel_file = request.FILES["excel_file"]
            
            wb = openpyxl.load_workbook(excel_file)
            worksheet = wb["Sheet1"]

            for row in worksheet.iter_rows():
                row_data = list()
                for cell in row:
                    row_data.append(str(cell.value))
                #create user
                username = row_data[1]
                password = BaseUserManager.make_random_password(self)

                user = User(username=username, email=row_data[3])
                user.password = make_password(password)
                try:
                    user.save()
                    #send email
                    msg = 'ID:{} \n Password: {}'.format(username, password)

                    send_mail('resultportal id and password', 
                        msg, 
                        'resultportal@gmail.com', 
                        [row_data[3]], 
                        fail_silently=False)

                    sv_user = User.objects.get(username=username)
                    #create user profile
                    UserProfileStudent.objects.create(
                        user=sv_user, 
                        is_student=True, 
                        is_teacher=False, 
                        name=row_data[0], 
                        department=row_data[2], 
                        rollnum=row_data[1])
                except:
                    continue

        return render(request, 'users/BulkUserCreation.html')

admin.site.register(UserProfileStudent, BulkUserCreate)
admin.site.register(UserProfileFaculty)