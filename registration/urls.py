from django.conf.urls import url
from . import views

app_name = 'registration'

urlpatterns = [
    url(r'^CreateRegistration/$', views.CreateRegistrationView, name="CreateRegistration")
]