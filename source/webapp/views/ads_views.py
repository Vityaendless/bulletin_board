from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q
from django.utils.http import urlencode
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib import messages

from ..models import Ad
from ..forms import SimpleSearchForm, AdForm
from ..helper import Message


class IndexView(ListView):
    model = Ad
    template_name = 'ads/index.html'
    context_object_name = 'ads'
    paginate_by = 10
    paginate_orphans = 1
    ordering = ('-published_at',)

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.search_form.is_valid():
            return self.search_form.cleaned_data['search']
        return None

    def dispatch(self, request, *args, **kwargs):
        self.search_form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(
                Q(title__icontains=self.search_value) |
                Q(description__icontains=self.search_value)
            )
        queryset = queryset.filter(status=2)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.search_form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search_value'] = self.search_value
        return context


class AdCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'ads/ad_create.html'
    model = Ad
    form_class = AdForm
    permission_required = 'webapp.add_ad'

    def form_valid(self, form):
        ad = form.save(commit=False)
        ad.author = self.request.user
        ad.save()
        return redirect('webapp:ad_view', pk=ad.pk)

    def has_permission(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.add_message(self.request, messages.WARNING, Message.get_no_access_message())
        return redirect('webapp:index')


class AdView(PermissionRequiredMixin, DetailView):
    model = Ad
    template_name = 'ads/ad_details.html'
    permission_required = 'webapp.view_ad'

    def has_permission(self):
        is_author = self.request.user == self.get_object().author
        is_approve = int(self.get_object().status) == 2
        is_delete = int(self.get_object().status) != 4
        is_other = int(self.get_object().status) not in [1, 3]
        if (is_approve or is_author) and (is_other or is_author) and is_delete:
            return True
        return False

    def handle_no_permission(self):
        messages.add_message(self.request, messages.WARNING, Message.get_no_access_message())
        return redirect('webapp:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.order_by('-created_at')
        return context


class AdUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'ads/ad_update.html'
    model = Ad
    form_class = AdForm
    permission_required = 'webapp.change_ad'

    def form_valid(self, form):
        ad = form.save(commit=False)
        if ad.status == '2':
            ad.status = 1
        ad.save()
        return redirect('accounts:profile', pk=ad.author.pk)

    def has_permission(self):
        is_author = self.request.user == self.get_object().author
        is_delete = int(self.get_object().status) != 4
        is_rejection = int(self.get_object().status) != 3
        if is_delete and is_rejection and is_author:
            return True
        return False

    def handle_no_permission(self):
        messages.add_message(self.request, messages.WARNING, Message.get_no_access_message())
        return redirect('webapp:ad_view', pk=self.get_object().pk)


class AdDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'ads/ad_delete.html'
    model = Ad
    permission_required = 'webapp.delete_ad'

    def post(self, request, *args, **kwargs):
        ad = get_object_or_404(Ad, pk=kwargs.get('pk'))
        ad.status = 4
        ad.save()
        return redirect('webapp:index')

    def has_permission(self):
        is_author = self.request.user == self.get_object().author
        is_delete = int(self.get_object().status) != 4
        if is_author and is_delete:
            return True
        return False

    def handle_no_permission(self):
        messages.add_message(self.request, messages.WARNING, Message.get_no_access_message())
        return redirect('webapp:ad_view', pk=self.get_object().pk)


class NoModerateAdsView(PermissionRequiredMixin, ListView):
    template_name = 'ads/no_moderate_list.html'
    context_object_name = 'ads'
    paginate_by = 10
    paginate_orphans = 1
    permission_required = 'webapp.see_no_moderate_ads'

    def handle_no_permission(self):
        messages.add_message(self.request, messages.WARNING, Message.get_no_access_message())
        return redirect('webapp:index')

    def get_queryset(self):
        return Ad.objects.filter(status=1).order_by('-created_at')
