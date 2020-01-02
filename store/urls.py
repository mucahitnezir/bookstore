from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('landing.urls')),
    path('auth/', include('auth.urls')),
    path('authors/', include('author.urls')),
    path('books/', include('book.urls')),
    path('publishers/', include('publisher.urls')),
    path('admin/', admin.site.urls),
]

# Admin
admin.site.site_header = settings.ADMIN_SITE_HEADER
admin.site.site_title = settings.ADMIN_SITE_HEADER
