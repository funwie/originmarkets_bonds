from django.urls import path
from applications.account.views import UserList, UserDetail

urlpatterns = [
    path('', UserList.as_view(), name='user-list'),
    path('<int:pk>/', UserDetail.as_view()),
]
