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


