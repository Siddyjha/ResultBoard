from django import forms
from . models import Message

class MessageForm(forms.Form):

    subject = forms.CharField(max_length=50, required=True)
    message     = forms.CharField(max_length=500, required=True)

    widgets = {
        'message': forms.Textarea(attrs={'rows': 15, 'cols': 30, 'style': 'resize:none;'}),
    }

    def save(self, sender, receiver, quoted, subject, msg):
        Message.objects.create(
            sender = sender,
            receiver = receiver,
            quoted = quoted,
            subject = subject,
            body = msg
        )