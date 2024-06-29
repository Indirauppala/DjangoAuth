from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetConfirmView
from . import views

urlpatterns = [
    path('', views.signup_view, name='signup'),
    path('home/', views.homePage, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='password_reset.html',
        email_template_name='password_reset_email.html',
        success_url='/password-reset-confirm/'), name='password_reset'),
    
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'), name='password_reset_done'),
    
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html',
        success_url='/password-reset-done/'), name='password_reset_confirm'),
    
    path('password-reset-done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_done.html'), name='password_reset_done'),
]
