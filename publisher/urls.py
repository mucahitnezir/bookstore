from django.urls import path

from .views import PublisherListView, PublisherDetailView

app_name = 'publisher'

urlpatterns = (
    path('', PublisherListView.as_view(), name='index'),
    path('<slug>/', PublisherDetailView.as_view(), name='detail')
)
