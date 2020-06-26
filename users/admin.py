from django.contrib import admin
from . models import User, UserProfileFaculty, UserProfileStudent

# Register your models here.
admin.site.register(User)
admin.site.register(UserProfileStudent)
admin.site.register(UserProfileFaculty)