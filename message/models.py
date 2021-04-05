from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    subject = models.CharField(max_length=50, blank=False) 
    body = models.CharField(max_length=500, blank=False)
    quoted = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='quoted_msg', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} to {}".format(self.sender, self.receiver)
