from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Message
from . forms import MessageForm
from courses.models import Course

#decorators
from resultportal.decorators import userprofile_student_required, student_required, first_login_password_changed
#urls
from resultportal.settings import student_login_url

@userprofile_student_required  
@student_required(login_url=student_login_url, redirect_field_name='')
@first_login_password_changed
def StudentSendMsgView(request, cid):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            course = Course.objects.get(cid=cid)
            print("hello under course")
            receiver = course.instructor.user
            sender = request.user
            quoted = None
            
            try:
                form.save(
                sender=sender, 
                receiver=receiver, 
                quoted=quoted, 
                subject=data.get('subject'), 
                msg=data.get('message')
                )
                messages.info(request, "Message Sent", extra_tags="message-tag")            
            except:
                messages.error(request, "Message Failed", extra_tags="message-tag")

    return redirect('student:DetailResultView', cid)

