from django.contrib import admin
from django.contrib.admin import ModelAdmin, register

from .models import Cart, Favorite, Ingredient, IngredientAmount, Recipe, Tag


@register(Tag)
class TagAdmin(ModelAdmin):
    list_display = ('name', 'slug', 'color')
    prepopulated_fields = {
        'slug': ('name',),
    }


@register(Ingredient)
class IngredientAdmin(ModelAdmin):
    list_display = ('name', 'measurement_unit')
    list_filter = ('name',)


@register(Recipe)
class RecipeAdmin(ModelAdmin):
    list_display = ('name', 'author')
    list_filter = ('author', 'name', 'tags')
    readonly_fields = ('count_favorites',)

    @admin.display(
        description='Число добавлений в избранное'
    )
    def count_favorites(self, obj):
        return obj.favorites.count()


@register(IngredientAmount)
class IngredientAmountAdmin(ModelAdmin):
    pass


@register(Favorite)
class FavoriteAdmin(ModelAdmin):
    pass


@register(Cart)
class CartAdmin(ModelAdmin):
    pass
