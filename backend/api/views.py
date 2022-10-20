from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from api.serializers import TagSerializer, IngredientSerializer, RecipeSerializer, CreateRecipeSerializer, ShortRecipeSerializer, FollowSerializer
from rest_framework import status, permissions
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from recipe.models import Favorite, Tag, Ingredient, User, Recipe, Shopping, Follow
from api.permissions import IsAdminOrReadOnly
from djoser.views import UserViewSet
from api.paginators import LimitPagePagination
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()

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

    @action(detail=True, methods=('post','delete'), permission_classes=(IsAuthenticated,))
    def subscribe(self, request, id=None):
        if request.method == 'POST':
            return self.add_obj(request, id)
        #elif request.method == 'DELETE':
            #return self.delete_obj(request.user, pk)           

    def add_obj(self, request, id):
        author = get_object_or_404(User, id=id)
        if request.user==author:
            return Response({'errors': 'Вы не можете подписываться на самого себя'}, status=status.HTTP_400_BAD_REQUEST)
        obj = Follow.objects.filter(user=request.user, author=author)
        if obj.exists():
            return Response({'errors': 'Вы уже подписаны на данного пользователя'}, status=status.HTTP_400_BAD_REQUEST)
        follow = Follow.objects.create(user=request.user, author=author)
        serializer=FollowSerializer(follow, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)
   

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

    @action(detail=True, methods=('post','delete'), permission_classes=(IsAuthenticated,))
    def favorite(self, request, pk=None):
        if request.method == 'POST':
            return self.add_obj(Favorite, request.user, pk)
        elif request.method == 'DELETE':
            return self.delete_obj(Favorite, request.user, pk)

    @action(detail=True, methods=('post','delete'), permission_classes=(IsAuthenticated,))
    def shopping_cart(self, request, pk=None):
        if request.method == 'POST':
            return self.add_obj(Shopping, request.user, pk)
        elif request.method == 'DELETE':
            return self.delete_obj(Shopping, request.user, pk)            
    
    def add_obj(self, model, user, pk):
        obj = model.objects.filter(user=user, recipe__id=pk)
        if obj.exists():
            return Response({'errors': 'Рецепт уже добавлен в список'}, status=status.HTTP_400_BAD_REQUEST)
        recipe = get_object_or_404(Recipe, id=pk)
        model.objects.create(user=user, recipe=recipe)
        serializer=ShortRecipeSerializer(recipe)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete_obj(self, model, user, pk):
        #user = request.user
        obj = model.objects.filter(user=user, recipe__id=pk)
        if obj.exists():
            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'errors': 'Рецепт уже удален!'},
                        status=status.HTTP_400_BAD_REQUEST)
        #recipe = get_object_or_404(Recipe, id=pk)
        #model.objects.create(user=user, recipe=recipe)
        #serializer=ShortRecipeSerializer(recipe)
        #return Response(serializer.data, status=status.HTTP_201_CREATED)