"""resultportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""
Admin site config
"""
from django.contrib import admin

admin.site.site_header = 'Result Board Admin'
admin.site.index_title = 'Result Board Admin'
admin.site.site_title = 'Result Board Admin'

from django.contrib import admin
from django.urls import path, include
from users.views import LandingPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPage),
    path('accounts/', include('allauth.urls')),
    path('users/', include('users.urls')),
    path('courses/',include('courses.urls')),
    path('student/', include('student.urls')),
    path('instructor/', include('instructor.urls')),
    path('result/', include('result.urls')),
    path('registration/', include('registration.urls'))
]
