from django.conf.urls import url
from . import views

app_name = "message"

urlpatterns = [
    url(r'^SendMsg/(?P<cid>[\w-]+)/$', views.StudentSendMsgView, name="StudentSendMsg")
]