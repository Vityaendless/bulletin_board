from django.urls import path

from .views import IndexView, AdCreateView, AdView, AdUpdateView, AdDeleteView


app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('ad/add/', AdCreateView.as_view(), name='ad_create'),
    path('ad/<int:pk>/', AdView.as_view(), name='ad_view'),
    path('ad/<int:pk>/update/', AdUpdateView.as_view(), name='ad_update_view'),
    path('ad/<int:pk>/delete/', AdDeleteView.as_view(), name='ad_delete_view'),
]
