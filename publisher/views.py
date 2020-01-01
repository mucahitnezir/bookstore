from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin

from book.models import Book
from publisher.models import Publisher


class PublisherListView(ListView):
    model = Publisher
    template_name = 'publisher/list.html'
    extra_context = {'title': _('Publishers')}

    def get_queryset(self):
        return Publisher.objects.all()


class PublisherDetailView(SingleObjectMixin, ListView):
    template_name = 'publisher/detail.html'
    paginate_by = 12

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return get_object_or_404(Publisher, slug=self.kwargs['slug'])

    def get_queryset(self):
        return Book.objects.filter(publisher=self.object)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = self.object.name
        return data
