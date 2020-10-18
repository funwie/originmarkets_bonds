from django.contrib import admin
from django.urls import path, include

api_patterns = [
    path('', include('applications.bond.urls')),
    path('users/', include('applications.account.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(api_patterns)),
]
