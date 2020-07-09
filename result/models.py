from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import UserProfileStudent
from courses.models import Course

class Result(models.Model):
    student       = models.ForeignKey(UserProfileStudent, on_delete=models.CASCADE)
    course        = models.ForeignKey(Course, on_delete=models.CASCADE)
    course_name   = models.CharField(max_length=254)
    exam_type     = models.CharField(max_length=254)
    weightage     = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(100)])
    student_marks = models.IntegerField()
    total_marks   = models.IntegerField()
    highest_marks = models.IntegerField(null=True, blank=True)
    avg_marks     = models.IntegerField(null=True, blank=True)
    date          = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course_name
    
    def get_contribution(self):
        return (self.weightage * self.student_marks)/self.total_marks