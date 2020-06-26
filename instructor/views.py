from django.shortcuts import render

# decorators
from resultportal.decorators import instructor_required

# Home view
@instructor_required(login_url='account_login')
def HomeView(request):
    return render(request, 'instructor/Home.html')
