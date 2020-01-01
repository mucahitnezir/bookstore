from django.urls import path

from book.views import BookDetailView

app_name = 'book'

urlpatterns = (
    path('<slug>/', BookDetailView.as_view(), name='detail'),
)
