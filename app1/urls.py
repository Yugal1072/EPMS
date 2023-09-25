
from django.urls import path
from app1.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('contact', contact, name='contact'),
    path('registration', registration, name='registration'),
    path('dashboard', dashboard, name='dashboard'),
    path('about', about, name='about'),
    path('blog', blog, name='blog'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),
    path('signup_page', signup_page, name='signup_page'),
    path('login_page/', login_page, name='login_page'),
    path('logout_page/', logout_page, name='logout_page'),
    path('feedback/', feedback, name='feedback'),
    
    
    #reset password
    # path('reset_password/',auth_views.PasswordResetView.as_view(template_name = "registration/password_reset.html"),name='reset_password'),

    # path('reset_pa ssword_sent/',auth_views.PasswordResetDoneView.as_view(template_name = "registration/password_reset_sent.html"),name='password_reset_done'), 

    # path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = "registration/password_reset_form.html"),name='password_reset_confirm'),
    
    # path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name = "registration/password_reset_done.html"),name='password_reset_complete'),

    # path('reset_password/',
    # auth_views.PasswordResetView.as_view(template_name = "accounts/password_reset.html"),
    # name='reset_password'),

    # path('reset_password_sent/',
    # auth_views.PasswordResetDoneView.as_view(template_name = "accounts/password_reset_sent.html"),
    # name='password_reset_done'), 
 
    # path('reset/<uidb64>/<token>/',
    # auth_views.PasswordResetConfirmView.as_view(template_name = "accounts/password_reset_form.html"),
    # name='password_reset_confirm'),
    
    # path('reset_password_complete/',
    # auth_views.PasswordResetCompleteView.as_view(template_name = "accounts/password_reset_done.html"),
    # name='password_reset_complete'),


    path('reset_password/',
    auth_views.PasswordResetView.as_view(template_name = "accounts/password_reset.html"),
    name='reset_password'),

    path('reset_password_sent/',
    auth_views.PasswordResetDoneView.as_view(template_name = "accounts/password_reset_sent.html"),
    name='password_reset_done'), 
 
    path('reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name = "accounts/password_reset_form.html"),
    name='password_reset_confirm'),
    
    path('reset_password_complete/',
    auth_views.PasswordResetCompleteView.as_view(template_name = "accounts/password_reset_done.html"),
    name='password_reset_complete'),

]