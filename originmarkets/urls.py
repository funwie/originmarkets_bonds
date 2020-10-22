from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

api_patterns = [
    path('', include('applications.bond.urls')),
    path('users/', include('applications.account.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(api_patterns)),
    path('',
         RedirectView.as_view(url='/api/'))
]
