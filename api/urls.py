from django.urls import *
from .views import *

urlpatterns = [
    path('post-api/', PostListCreateAPIView.as_view()),
    path('post-api/<int:pk>', PostRetreieveUpdateDestroyAPIView.as_view()),
    path('user-api/', UserListAPIView.as_view()),
    path('user-api/<int:pk>/', UserRetreiveAPIView.as_view())
]