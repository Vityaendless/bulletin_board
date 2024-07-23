from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import ProfileView, RegisterView, UserEditView, UserPasswordChangeView


app_name = 'accounts'


urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('registration/', RegisterView.as_view(), name='registration'),
    path('profile/<int:pk>/edit/', UserEditView.as_view(), name='edit_user'),
    path('profile/<int:pk>/password_change/', UserPasswordChangeView.as_view(), name='user_password_change'),
]
