
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('home.urls')),
    path('user/', include('user_profile.urls')),
    path('chat/', include('chat.urls')),
    path('post/', include('post.urls')),
    path('api/', include('api.urls')),
    path('auth-api/', include('rest_auth.urls')),
    path('auth-api/registration', include('rest_auth.registration.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)