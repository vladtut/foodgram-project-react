from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(
        max_length=200,
        help_text='введите название тега',
        verbose_name='название тега')
    slug = models.SlugField(
        max_length=200,
        unique=True,
        help_text='введите слаг',
        verbose_name='слаг')
    color = models.CharField(
        max_length=7,
        help_text='введите цвет',
        verbose_name='цвет')

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(
        max_length=200,
        help_text='введите название ингредиента',
        verbose_name='название ингредиента')
    measurement_unit = models.CharField(
        max_length=10,
        help_text='введите название ингредиента',
        verbose_name='название ингредиента')

    def __str__(self):
        return self.name


class Ingredient_amount(models.Model):
    ingredient = models.ForeignKey(
        'Ingredient',
        on_delete=models.CASCADE,
        related_name='recipe_ingredient',
        help_text='введите название ингредиента',
        verbose_name='название ингредиента',
    )
    recipe = models.ForeignKey(
        'Recipe',
        on_delete=models.CASCADE,
        related_name='recipe_ingredient',
        help_text='введите название рецепта',
        verbose_name='название рецепта',
    )
    amount = models.PositiveIntegerField(
        help_text='введите количество',
        verbose_name='количество')


class Recipe(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text='введите название рецепта',
        verbose_name='название рецепта')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        help_text='введите автора',
        verbose_name='Автор',
    )
    image = models.ImageField(
        'Картинка',
        upload_to='recipes/',
        blank=True
    )
    text = models.TextField(
        help_text='введите текст описания ',
        verbose_name='текст описания')
    ingredients = models.ManyToManyField(
        'Ingredient',
        help_text='введите ингредиент',
        verbose_name='ингредиент',
        through='Ingredient_amount'
    )
    tags = models.ManyToManyField(
        'Tag',
        help_text='введите тэг',
        verbose_name='тэг',
    )
    cooking_time = models.PositiveIntegerField(
        help_text='введите время приготовления',
        verbose_name='время приготовления')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        help_text='ссылка на объект пользователя, который подписывается',
        verbose_name='Пользователь',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        help_text='ссылка на объект пользователя, на которого подписываются',
        verbose_name='Автор',
    )


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorite',
        help_text='ссылка на объект пользователя, который подписывается',
        verbose_name='Автор',
    )
    recipe = models.ForeignKey(
        'Recipe',
        on_delete=models.CASCADE,
        related_name='favorite',
        help_text='введите название рецепта',
        verbose_name='название рецепта',
    )


class Shopping(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shopping',
        help_text='ссылка на объект пользователя, который подписывается',
        verbose_name='Автор',
    )
    recipe = models.ForeignKey(
        'Recipe',
        on_delete=models.CASCADE,
        related_name='shopping',
        help_text='введите название рецепта',
        verbose_name='название рецепта',
    )
