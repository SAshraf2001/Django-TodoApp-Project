
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authApp.urls')),
    path('task/', include('taskApp.urls')),
]
