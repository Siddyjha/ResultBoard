from django.conf.urls import url
from . import views

app_name = "student"

urlpatterns = [
    url(r'^Home/$', views.StudentHomeView, name="Home"),
    url(r'^RegistrationStatus/$', views.RegistrationStatusView , name="RegistrationStatus"),
    url(r'^RegisteredCourses/$', views.RegisteredCoursesView, name="RegisteredCourses"),
    url(r'^ViewResults/$', views.AllResultView, name="ViewResults"),
    url(r'^EditProfile/$', views.EditUserProfileView, name="EditProfile"),
    url(r'^detail/(?P<cid>[\w-]+)/$', views.DetailResultView, name='DetailResultView')
]