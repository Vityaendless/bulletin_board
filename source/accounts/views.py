from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth import get_user_model


class ProfileView(DetailView):
    model = get_user_model()
    template_name = 'profile.html'
    context_object_name = 'user_obj'
