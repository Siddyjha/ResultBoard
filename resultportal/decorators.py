from functools import wraps
from django.contrib import messages
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.shortcuts import redirect
from django.contrib import messages
from django.core.exceptions import PermissionDenied

from django.shortcuts import resolve_url
from urllib.parse import urlparse
#from resultportal.settings import config
import resultportal.settings as settings
import requests

default_message = ''
unauthenticated_message = 'User already logged in'


def user_passes_test(test_func, login_url=None, redirect_field_name=REDIRECT_FIELD_NAME, message=default_message):

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not test_func(request.user):
                messages.add_message(request, messages.ERROR, message)
            if test_func(request.user):
                return view_func(request, *args, **kwargs)
            path = request.build_absolute_uri()
            resolved_login_url = resolve_url(login_url or settings.LOGIN_URL)
            # If the login url is the same scheme and net location then just
            # use the path as the "next" url.
            login_scheme, login_netloc = urlparse(resolved_login_url)[:2]
            current_scheme, current_netloc = urlparse(path)[:2]
            if ((not login_scheme or login_scheme == current_scheme) and
                    (not login_netloc or login_netloc == current_netloc)):
                path = request.get_full_path()
            return redirect_to_login(
                path, resolved_login_url, redirect_field_name)
        return _wrapped_view
    return decorator

# superuser required
def superuser_required(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/login', message=default_message):

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_superuser and u.is_authenticated,
        login_url=login_url,
        redirect_field_name=REDIRECT_FIELD_NAME,
        message=message        
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator

# staff required
def staff_required(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/login', message=default_message):

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_staff and u.is_authenticated,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
        message=message
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator

# login not required
def unauthenticated_required(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME, home_url='/', message=default_message):

    actual_decorator = user_passes_test(
        lambda u: not u.is_active and not u.is_authenticated,
        login_url=home_url,
        redirect_field_name=redirect_field_name,
        message=message
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator

# student login required
def student_required(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/login', message=default_message):

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.userprofilestudent.is_student and u.is_authenticated and not u.userprofilestudent.is_teacher,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
        message=message
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator

#  instructor login required
def instructor_required(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/login', message=default_message):

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.userprofilefaculty.is_teacher and u.is_authenticated and not u.userprofilefaculty.is_student,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
        message=message
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator

# student must have a user profile
def userprofile_student_required(function):
    def wrap(request, *args, **kwargs):
        try:
            request.user
        except:
            return redirect('account_login')
        try:
            request.user.userprofilestudent
            return function(request, *args, **kwargs)
        except:
            try:
                request.user.userprofilefaculty
                return redirect('instructor:HomeView')
            except:
                messages.error(request, "You must have valid user profile to continue using this portal", extra_tags="userprofile_error")
                return redirect('users:CreateProfile')
        
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    wrap.__dict__ = function.__dict__
    return wrap 
