from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [    

    path('', include('api.urls')),
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls)
]

handler404 = 'core.views.page_not_found'
handler500 = 'core.views.server_error'