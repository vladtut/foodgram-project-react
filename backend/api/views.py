from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from api.serializers import TagSerializer, IngredientSerializer
from rest_framework import permissions
from rest_framework.viewsets import ReadOnlyModelViewSet
from recipe.models import Tag, Ingredient, User
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