from imp import source_from_cache
from importlib.util import source_hash
from rest_framework import serializers
from recipe.models import Tag, Ingredient, Ingredient_amount, Recipe, Follow, Favorite, Shopping
import base64  
from django.core.files.base import ContentFile
from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer, UserSerializer

User = get_user_model()

class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        # Если полученный объект строка, и эта строка 
        # начинается с 'data:image'...
        if isinstance(data, str) and data.startswith('data:image'):
            # ...начинаем декодировать изображение из base64.
            # Сначала нужно разделить строку на части.
            format, imgstr = data.split(';base64,')  
            # И извлечь расширение файла.
            ext = format.split('/')[-1]  
            # Затем декодировать сами данные и поместить результат в файл,
            # которому дать название по шаблону.
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super().to_internal_value(data)

class CustomUserCreateSerializer(UserCreateSerializer):
    # author = SlugRelatedField(slug_field='username', read_only=True)
    username = serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        
#        extra_kwargs = {
#            'username':{'required': True},
#            'email':{'required': True},
#            'first_name':{'required': True},
#            'last_name':{'required': True},
#            'password':{'required': True},
#        }

class CustomUserSerializer(UserSerializer):
    # author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = User
        fields = ['email', 'id', 'username', 'first_name', 'last_name']
        

class TagSerializer(serializers.ModelSerializer):
    # author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Tag

class IngredientSerializer(serializers.ModelSerializer):
    # author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Ingredient

class Ingredient_amountSerializer(serializers.ModelSerializer):
    # author = SlugRelatedField(slug_field='username', read_only=True)
    id = serializers.ReadOnlyField(source='ingredient.id')
    name = serializers.ReadOnlyField(source='ingredient.name')
    unit = serializers.ReadOnlyField(source='ingredient.unit')

    class Meta:
        fields = ('id','name','unit','amount')
        model = Ingredient_amount

class CreateIngredient_amountSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    amount = serializers.IntegerField()

    class Meta:
        fields = ('id','amount')
        model = Ingredient_amount        

class RecipeSerializer(serializers.ModelSerializer):
    # author = SlugRelatedField(slug_field='username', read_only=True)
    image = Base64ImageField(required=False, allow_null=True)
    tags = TagSerializer(many=True, read_only=True)
    ingredients = Ingredient_amountSerializer(source='recipe_ingredient',many=True, read_only=True)
    author = CustomUserSerializer(many=False, read_only=True) 
    class Meta:
        fields = ['id', 'image', 'name', 'text', 'cooking_time', 'author', 'ingredients', 'tags']
        model = Recipe

class CreateRecipeSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(many=False, read_only=True)
    image = Base64ImageField(required=False, allow_null=True)
    #tags = TagSerializer(many=True, read_only=True)
    ingredients = CreateIngredient_amountSerializer(many=True)
     
    class Meta:
        model = Recipe
        fields = ['image', 'name', 'text', 'cooking_time', 'author', 'ingredients', 'tags']

class FollowSerializer(serializers.ModelSerializer):
    # author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Follow

class FollowSerializer(serializers.ModelSerializer):
    # author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Favorite

class FollowSerializer(serializers.ModelSerializer):
    # author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Shopping




