from rest_framework.routers import DefaultRouter
from django.urls import include, path
from api.views import TagViewSet ,IngredientViewSet, CustomUserViewSet, RecipeViewSet

router = DefaultRouter()

router.register('tags', TagViewSet, basename='tags')
router.register('ingredients', IngredientViewSet, basename='ingredients')
router.register('users', CustomUserViewSet, basename='users')
router.register('recipes', RecipeViewSet, basename='recipes')
app_name = 'api'
urlpatterns = [  
    path('auth/', include('djoser.urls.authtoken')),
    path('',include(router.urls)),
    path('', include('djoser.urls')),
]