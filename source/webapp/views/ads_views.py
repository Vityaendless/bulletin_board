from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q
from django.utils.http import urlencode
from django.shortcuts import redirect
from django.urls import reverse_lazy

from ..models import Ad
from ..forms import SimpleSearchForm, AdForm


class IndexView(ListView):
    model = Ad
    template_name = 'ads/index.html'
    context_object_name = 'ads'
    paginate_by = 10
    paginate_orphans = 1
    ordering = ('-created_at',)

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
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.search_form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search_value'] = self.search_value
        return context


class AdCreateView(CreateView):
    template_name = 'ads/ad_create.html'
    model = Ad
    form_class = AdForm

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('webapp:index')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        ad = form.save(commit=False)
        ad.author = self.request.user
        ad.save()
        return redirect('webapp:ad_view', pk=ad.pk)


class AdView(DetailView):
    model = Ad
    template_name = 'ads/ad_details.html'


class AdUpdateView(UpdateView):
    template_name = 'ads/ad_update.html'
    model = Ad
    form_class = AdForm


class AdDeleteView(DeleteView):
    template_name = 'ads/ad_delete.html'
    model = Ad
    success_url = reverse_lazy('webapp:index')
