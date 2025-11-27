from django.urls import path
from rest_framework.routers import SimpleRouter

from applications.users.views import LoginAPIView
from applications.users.viewsets import CreateUserViewSet


users_router = SimpleRouter()

users_router.register('users', CreateUserViewSet, basename='users')

users_urlpatterns = [
    path('login/', LoginAPIView.as_view()),
]
