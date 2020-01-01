from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

from book.models import Book


class BookDetailView(DetailView):
    model = Book
    template_name = 'book/detail.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Book, slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        data = super().get_context_data()
        data['title'] = self.object.name
        return data
