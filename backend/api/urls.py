from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import TagViewSet

router = DefaultRouter()

router.register('tags', TagViewSet, basename='tags')
app_name = 'api'
urlpatterns = [  
    path('users/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('',include(router.urls)),
]