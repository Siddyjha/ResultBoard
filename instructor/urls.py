from django.conf.urls import url
from . import views

app_name="instructor"

urlpatterns = [
    url(r'^Home/$', views.HomeView, name="HomeView")
]