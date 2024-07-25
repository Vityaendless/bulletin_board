from django.shortcuts import redirect, reverse
from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

from .forms import MyUserCreationForm, UserChangeForm
from webapp.helper import Message


class ProfileView(DetailView):
    model = get_user_model()
    template_name = 'profile.html'
    context_object_name = 'user_obj'
    paginate_related_by = 10
    paginate_related_orphans = 1

    def get_context_data(self, **kwargs):
        if self.request.user.pk == self.kwargs.get('pk'):
            ads = self.object.ads.filter(Q(status='1') | Q(status='2') | Q(status='3'))
        else:
            ads = self.object.ads.filter(status='2')
        paginator = Paginator(ads, self.paginate_related_by, orphans=self.paginate_related_orphans)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        kwargs['page_obj'] = page
        kwargs['ads'] = page.object_list
        kwargs['is_paginated'] = page.has_other_pages()
        return super().get_context_data(**kwargs)


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
