from . models import Message

class Inbox():
    
    def __init__(self, user):
        self.user = user
        self.messages = Message.objects.filter(receiver=self.user).order_by('date').reverse()

    def get_messages(self):
        return self.messages