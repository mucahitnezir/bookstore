from django.urls import path

from landing.views import HomeView

app_name = 'landing'

urlpatterns = (
    path('', HomeView.as_view(), name='home'),
)
