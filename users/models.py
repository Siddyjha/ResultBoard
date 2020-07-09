from django.db import models
from django.contrib.auth.models import User

class UserProfileFaculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    department_choice = [
        ('CSE', 'COMPUTER SCIENCE ENGINEERING'),
        ('ECE', 'ELECTRONICS AND COMMUNICATION ENGINEERING'),
    ]

    name = models.CharField(max_length=254)
    department = models.CharField(max_length=254, choices=department_choice, default='CSE')

    def __str__(self):
        return self.name

class UserProfileStudent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    def_pass_changed = models.BooleanField(default=False)

    department_choice = [
        ('CSE', 'COMPUTER SCIENCE ENGINEERING'),
        ('ECE', 'ELECTRONICS AND COMMUNICATION ENGINEERING'),
    ]

    name = models.CharField(max_length=254)
    department = models.CharField(max_length=254, choices=department_choice, default='CSE')
    rollnum = models.IntegerField(unique=True)
    semester = models.IntegerField(choices=list(zip(range(1,9), range(1,9))), default=1)

    def __str__(self):
        return self.name

class DummyModel(models.Model):
    class Meta:
        verbose_name_plural = 'model'