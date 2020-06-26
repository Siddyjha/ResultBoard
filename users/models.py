from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

# Create your models here.

class UserManager(BaseUserManager):

    def _create_user(self, email, password, is_staff, is_superuser,  **extra_fields):
        if not email:
            raise ValueError('users must have a valid email')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email = email,
            is_staff = is_staff,
            is_active = True,
            is_superuser = is_superuser,
            last_login = now,
            date_joined = now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, True, True, **extra_fields)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length = 254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)

    def get_email(self):
        return self.email

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