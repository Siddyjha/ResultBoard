from django.shortcuts import render, redirect
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required

# Handles adding user information after new user signup
@login_required(login_url='account_login')
def CreateProfileView(request):
    try:
        request.user.userprofilestudent
        return redirect('student:EditProfile')
    except:
        if request.method == 'POST':
            form = UserProfileForm(request.POST)
            if form.is_valid():
                NewProfileForm = form.save(commit=False)
                user = request.user
                NewProfileForm.user = user
                NewProfileForm.is_teacher = False
                NewProfileForm.is_student = True
                NewProfileForm.save()
                return redirect('student:ViewResults')
        else:
            form = UserProfileForm()

        context = {
            'NewProfileForm': form
        }

        return render(request, 'users/CreateProfile.html', context)

# viewing user profile
def UserProfileView(request):
    user = (request.user).userprofilestudent
    context = {
        'user': user
    }
    return render(request, 'users/UserProfile.html', context)

# test home view
@login_required(login_url='account_login')
def HomeView(request):
    try:
        request.user.userprofilestudent
        return redirect('student:ViewResults')
    except:
        try:
            request.user.userprofilefaculty
            return redirect('instructor:HomeView')
        except:
            return redirect('users:CreateProfile')
    

def LandingPage(request):
    return redirect('account_login')