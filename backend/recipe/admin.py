from django.contrib import admin

from .models import Tag, Ingredient, Ingredient_amount, Recipe, Follow, Favorite, Shopping


class TagAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug', 'color')
    list_editable = ('color',)
    search_fields = ('name',)
    #list_filter = ('name',)
    empty_value_display = '-пусто-'


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'unit')
    list_editable = ('unit',)
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


class Ingredient_amountAdmin(admin.ModelAdmin):
    list_display = ('pk', 'ingredient', 'recipe', 'quantity')
    #ist_editable = ('ingredient', 'recipe', 'quantity ',)
    #search_fields = ('recipe')
    list_filter = ('recipe',)
    empty_value_display = '-пусто-'


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'author', 'image', 'description', 'time')
    #list_editable = ('c',)
    search_fields = ('title',)
    list_filter = ('author', 'title', 'tag')
    empty_value_display = '-пусто-'


class FollowAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'author')
    #list_editable = ('',)
    #search_fields = ('author',)
    #list_filter = ('author',)
    empty_value_display = '-пусто-'


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'recipe')
    #list_editable = ('user', 'recipe',)
    #search_fields = ('user', 'recipe',)
    list_filter = ('user',)
    empty_value_display = '-пусто-'


class ShoppingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'recipe')
    #list_editable = ('user', 'recipe',)
    #search_fields = ('user',)
    list_filter = ('user', )
    empty_value_display = '-пусто-'


admin.site.register(Tag, TagAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Ingredient_amount, Ingredient_amountAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Follow, FollowAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Shopping, ShoppingAdmin)

