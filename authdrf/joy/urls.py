from django.urls import path, include
from joy import views, serializers
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'poems', views.PoemViewSet, basename='poem')
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'groups', views.GroupViewSet, basename='group')

urlpatterns = [
    path('', include(router.urls)),
]

