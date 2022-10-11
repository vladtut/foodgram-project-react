from rest_framework.routers import DefaultRouter
from django.urls import include, path
from api.views import TagViewSet ,IngredientViewSet, CustomUserViewSet

router = DefaultRouter()

router.register('tags', TagViewSet, basename='tags')
router.register('ingredients', IngredientViewSet, basename='ingredients')
router.register('users', CustomUserViewSet, basename='users')
app_name = 'api'
urlpatterns = [  
    path('users/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('',include(router.urls)),
]