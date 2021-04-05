from django.conf.urls import url
from . import views

app_name="instructor"

urlpatterns = [
    url(r'^Home/$', views.HomeView, name="HomeView"),
    url(r'^ResultHistory/$', views.SentResultView, name="SentResultView"),
    url(r'^get_result_preview/$', views.ResultPreview, name="ResultPreview"),
    url(r'^Inbox/$', views.InstructorInboxView, name="Inbox")
]