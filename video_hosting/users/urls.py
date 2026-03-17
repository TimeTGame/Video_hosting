from django.urls import path

from . import views


app_name = 'users'

urlpatterns = [
    path('register/', views.register_view, name='register_view'),
    path('login/', views.login_view, name='login_view'),
    path('profile/', views.profile_view, name='profile_view'),
    path('account-details/', views.account_details, name='account_details'),
    path(
        'edit-account-details/',
        views.edit_account_details,
        name='edit_account_details',
    ),
    path(
        'update-account-details/',
        views.update_account_details,
        name='update_account_details',
    ),
    path('logout/', views.logout_view, name='logout_view'),
]
