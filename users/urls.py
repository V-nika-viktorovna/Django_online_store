from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, email_verificqation

app_name = UsersConfig.name

urlpatterns = [
    path('users/login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('users/logout/', LogoutView.as_view(next_page='catalog:home'), name='logout'),
    path('users/register/', RegisterView.as_view(), name='register'),
    path('email-confirm/<str:token>/', email_verificqation, name='email-confirm'),
]
