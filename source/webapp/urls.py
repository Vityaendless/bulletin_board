from django.urls import path

from .views import IndexView, AdCreateView, AdView


app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/add/', AdCreateView.as_view(), name='ad_create'),
    path('product/<int:pk>/', AdView.as_view(), name='ad_view'),
]
