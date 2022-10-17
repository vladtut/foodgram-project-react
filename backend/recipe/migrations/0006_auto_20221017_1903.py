# Generated by Django 2.2.16 on 2022-10-17 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0005_auto_20221016_1329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(help_text='введите ингредиент', through='recipe.Ingredient_amount', to='recipe.Ingredient', verbose_name='ингредиент'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(help_text='введите ингредиент', through='recipe.Ingredient_amount', to='recipe.Ingredient', verbose_name='ингредиент'),
        ),        
    ]
