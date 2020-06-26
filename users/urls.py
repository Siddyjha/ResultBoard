from django.conf.urls import url
from . import views

app_name = 'users'

urlpatterns = [
    url(r'^CreateProfile/$', views.CreateProfileView, name = "CreateProfile"),
    url(r'^UserProfile/$', views.UserProfileView, name = "UserProfile"),
    url(r'^Home/$', views.HomeView, name="Home")
]