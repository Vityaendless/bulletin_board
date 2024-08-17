from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from .views import ModerationView, LogoutView, CommentModelViewSet


app_name = 'api_v1'

router = routers.DefaultRouter()
router.register(r'comments', CommentModelViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('moderation/<int:pk>/', ModerationView.as_view(), name='moderation'),
    path('login/', obtain_auth_token, name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
