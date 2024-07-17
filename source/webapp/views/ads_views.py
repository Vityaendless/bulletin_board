from django.views.generic import ListView

from ..models import Ad


class IndexView(ListView):
    model = Ad
    template_name = 'ads/index.html'
    context_object_name = 'ads'
