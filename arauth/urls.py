from django.urls import path
from . import views

app_name = 'arauth'

urlpatterns = [
    path('login', views.arlogin, name='login'),
    path('logout', views.arlogout, name='logout'),
    path('register', views.register, name='register'),
    path('captcha', views.send_email_captcha, name='email_captcha')


]
