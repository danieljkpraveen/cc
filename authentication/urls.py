from django.urls import path
from django.contrib.auth import views as auth_views
from authentication.forms import CustomPasswordResetForm, CustomSetPasswordForm

from . import views
from .forms import LoginForm


app_name = 'authentication'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html',
         authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             form_class=CustomPasswordResetForm,
             template_name='authentication/password_reset.html',
             email_template_name='authentication/password_reset_email.html',
             success_url='password-reset-done/'
         ),
         name='password-reset'),
    path('password-reset-done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='authentication/password_reset_done.html'
         ),
         name='password-reset-done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='authentication/password_reset_confirm.html', form_class=CustomSetPasswordForm), name='password-reset-confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='authentication/password_reset_complete.html'), name='password-reset-complete'),
]
