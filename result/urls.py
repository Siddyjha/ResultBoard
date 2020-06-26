from django.conf.urls import url
from . import views

app_name = 'result'

urlpatterns = [
    url(r'^CreateResult/$', views.CreateResult, name="CreateResult"),
    url(r'^GetCourseName/$', views.GetCourseName, name="GetCourseName")
]