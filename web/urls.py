"""
Web URL's
"""
#from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from allauth.account import views as aa_views
from . import views

urlpatterns = [
    path('', views.index, name="IndexView"),
    #path('register/', views.register, name="RegisterView"),
    #path('signup/' aa_views.SignupView.as_view(template_name='reg/reg.html'), name="SignupView")
    #path('login/', aa_views.LoginView.as_view(template_name='login/login.html'), name="LoginView"),
    #path('logout/', aa_views.LogoutView.as_view(template_name='logout/logout.html'), name="LogoutView"),
    path('user/', views.UserInfo, name="UserInfoView"),
    path('guest/new/', views.NewGuestView, name='NewGuestView')
]
