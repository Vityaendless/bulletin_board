from django.shortcuts import redirect, reverse
from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages

from .forms import MyUserCreationForm, UserChangeForm
from webapp.helper import Message


class ProfileView(DetailView):
    model = get_user_model()
    template_name = 'profile.html'
    context_object_name = 'user_obj'


class RegisterView(CreateView):
    model = get_user_model()
    form_class = MyUserCreationForm
    template_name = 'registration.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('webapp:index')


class UserEditView(UserPassesTestMixin, UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = 'user_update.html'
    context_object_name = 'user_obj'

    def test_func(self):
        return self.request.user.pk == self.kwargs.get('pk')

    def handle_no_permission(self):
        messages.add_message(self.request, messages.WARNING, Message.get_no_access_message())
        return redirect('accounts:profile', pk=self.kwargs.get('pk'))

    def get_success_url(self):
        return reverse('accounts:profile', kwargs={'pk': self.object.pk})


class UserPasswordChangeView(UserPassesTestMixin, PasswordChangeView):
    template_name = 'user_password_change.html'

    def test_func(self):
        return self.request.user.pk == self.kwargs.get('pk')

    def handle_no_permission(self):
        messages.add_message(self.request, messages.WARNING, Message.get_no_access_message())
        return redirect('accounts:profile', pk=self.kwargs.get('pk'))

    def get_success_url(self):
        return reverse('accounts:profile', kwargs={'pk': self.request.user.pk})
