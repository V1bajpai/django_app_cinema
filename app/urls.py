from django.contrib.auth import views as auth_views
from django.urls import path, include
from app import views
from app.forms import LoginForm

urlpatterns = [
    path('', views.home),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm),
         name='login'),
    path('accounts/profile/', views.ProfileView.as_view(), name='profile'),

]
