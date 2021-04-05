from django.db import models
from users.models import UserProfileStudent
from courses.models import Course

# Create your models here.
class Registration(models.Model):
    
    student_id = models.ForeignKey(UserProfileStudent, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return "{id}".format(id=self.pk)

class ApprovedRegistrations(models.Model):
    rollnum = models.IntegerField(blank=False)
    semester = models.IntegerField(choices=list(zip(range(1,9), range(1,9))), default=1)

    def __str__(self):
        return "{}".format(self.rollnum)
