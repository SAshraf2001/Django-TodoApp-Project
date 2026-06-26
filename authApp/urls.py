from django.urls import path
from authApp import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('about/', views.about_view, name='about'),
    path('signup/', views.signup_view, name='signup')
]