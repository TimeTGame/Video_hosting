__all__ = []

from django.contrib.auth import logout
from django.shortcuts import redirect


def active_user_middleware(get_response):
    def middleware(request):
        if request.user.is_authenticated and not request.user.is_active:
            logout(request)
            return redirect('users:login_view')
        return get_response(request)
    return middleware
