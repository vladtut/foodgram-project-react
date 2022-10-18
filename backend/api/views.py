from django.shortcuts import render
from rest_framework.pagination import LimitOffsetPagination
from api.serializers import TagSerializer, IngredientSerializer, RecipeSerializer, CreateRecipeSerializer
from rest_framework import permissions
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from recipe.models import Tag, Ingredient, User, Recipe
from api.permissions import IsAdminOrReadOnly
from djoser.views import UserViewSet
from api.paginators import LimitPagePagination

# Create your views here.
class TagViewSet(ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAdminOrReadOnly,)
    # pagination_class = LimitOffsetPagination

class IngredientViewSet(ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (IsAdminOrReadOnly,)
    # pagination_class = LimitOffsetPagination

class CustomUserViewSet(UserViewSet):
    #queryset = User.objects.all()
    #serializer_class = CustomUserSerializer
    #permission_classes = (IsAdminOrReadOnly,)
    pagination_class = LimitPagePagination

class RecipeViewSet(ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = LimitPagePagination

    def get_serializer_class(self):
        if (self.action == 'list' or self.action == 'retrieve'):
            return RecipeSerializer
        return CreateRecipeSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)