from django.db import models
from users.models import UserProfileFaculty

class ResultHistory(models.Model):
    instructor = models.ForeignKey(UserProfileFaculty, on_delete=models.CASCADE)
    excel_file = models.FileField(upload_to='docs/')
    created_on = models.DateTimeField(auto_now_add=True)
    exam_type = models.CharField(max_length=254)

    def __str__(self):
        return self.instructor.name

    def get_date(self):
        return self.created_on.strftime('%d/%m/%Y')