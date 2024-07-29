from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import ModerationView


app_name = 'api_v1'


urlpatterns = [
    path('moderation/<int:pk>/', ModerationView.as_view(), name='moderation'),
]
