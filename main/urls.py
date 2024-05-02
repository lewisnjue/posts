from django.urls import path 
from . import views 
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',LoginView.as_view(template_name='main/login.html'),name='login'),
    path('logout/',views.logoutview,name='logout'),
    path('create_post/',views.create_post,name='create_post'),
   path('reset_password/', auth_views.PasswordResetView.as_view(template_name='main/password_reset.html'), name='password_reset'),
    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(template_name='main/password_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='main/password_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='main/password_done.html'), name='password_reset_complete'),
]

"""
subbit email form    // PasswordResetView.as_view()
Email sent  success messange  // passwordResetDoneView.as_view()
Link to Password Reset Form in email // passwordresetconfirmview.as_view()
password successfully changed message // passwordResetcompleteview.as_view()
"""