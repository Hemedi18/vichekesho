from django.urls import path
from django.contrib.auth.views import LogoutView, PasswordChangeDoneView
from .views import register, CustomLoginView, account_view, CustomPasswordChangeView

app_name = 'users'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logged_out.html'), name='logout'),
    path('account/', account_view, name='account'),
    path('account/change-password/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('account/change-password/done/', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),
]