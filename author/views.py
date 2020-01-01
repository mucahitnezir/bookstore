from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin

from author.models import Author
from book.models import Book


class AuthorListView(ListView):
    model = Author
    template_name = 'author/list.html'
    paginate_by = 20
    extra_context = {'title': _('Authors')}

    def get_queryset(self):
        return Author.objects.all()


class AuthorDetailView(SingleObjectMixin, ListView):
    template_name = 'author/detail.html'
    paginate_by = 12

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return get_object_or_404(Author, slug=self.kwargs['slug'])

    def get_queryset(self):
        return Book.objects.filter(authors=self.object)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = self.object.name
        return data
