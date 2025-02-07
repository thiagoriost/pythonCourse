from django.urls import include, path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from .views import RegisterView



urlpatterns = [
    path(
        'login/',
        # LoginView.as_view(template_name='app_users/templates/users_template/login.html'),
        LoginView.as_view(template_name='users_template/login.html'),
        name='login'
    ),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('logout/', auth_views.LogoutView.as_view(next_page="login/"), name='logout'),
    path('registro/', RegisterView.as_view(), name='register'),
]
