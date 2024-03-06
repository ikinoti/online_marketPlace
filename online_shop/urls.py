from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('frontPage.urls')),
    path('items/', include('item.urls')),
    # path('contact/', contact, name='contact'),
    path('dashboard/', include('dashboard.urls')),
    path('indox/', include('conversation.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
