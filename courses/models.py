from django.db import models
from users.models import UserProfileFaculty
from django.contrib.auth import get_user_model

def get_sentinel_user():
    return get_user_model().objects.get_or_create(email="deleted")[0]

class Course(models.Model):
    cid = models.CharField(max_length=10, unique=True, verbose_name='Course ID')
    name = models.CharField(max_length=254)
    semester = models.IntegerField(choices=list(zip(range(1,9), range(1,9))), default=1)
    instructor = models.ForeignKey(UserProfileFaculty, on_delete=models.SET(get_sentinel_user))
    

    def __str__(self):
        return self.cid 