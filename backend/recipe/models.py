from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, RegexValidator
from django.db.models import (CASCADE, CharField, DateTimeField, ForeignKey,
                              ImageField, ManyToManyField, Model,
                              PositiveIntegerField, SlugField, TextField,
                              UniqueConstraint)

User = get_user_model()


class Ingredient(Model):
    measurement_unit = CharField(
        verbose_name='Единицы измерения',
        max_length=200,
    )
    name = CharField(
        verbose_name='Ингредиент',
        max_length=200,
    )

    def __str__(self) -> str:
        return f'{self.name}, {self.measurement_unit}'

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ('name',)
        constraints = (
            UniqueConstraint(
                name='Unique_measure_for_ingredient',
                fields=('name', 'measurement_unit'),
            ),
        )


class IngredientAmount(Model):
    amount = PositiveIntegerField(
        verbose_name='Количество',
        validators=(
            MinValueValidator(1, 'Не может быть меньше 1.'),
        ),
    )
    ingredients = ForeignKey(
        to=Ingredient,
        on_delete=CASCADE,
        related_name='recipe',
        verbose_name='Ингредиенты, связанные с рецептом',
    )
    recipe = ForeignKey(
        to='Recipe',
        on_delete=CASCADE,
        related_name='ingredient',
        verbose_name='Рецепты, содержащие ингредиенты',
    )

    def __str__(self) -> str:
        return f'{self.recipe}: {self.amount}, {self.ingredients}'

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Количество ингредиентов'
        ordering = ('recipe',)
        constraints = (
            UniqueConstraint(
                name='Unique_ingredient_in_recipe',
                fields=('ingredients', 'recipe')
            ),
        )


class Tag(Model):
    color = CharField(
        verbose_name='Код цвета',
        max_length=7,
        default='#ffffff',
        validators=[
            RegexValidator(
                regex=r"^#(?:[0-9a-fA-F]{3}){1,2}$",
            )
        ]
    )

    name = CharField(
        verbose_name='Тег',
        max_length=200,
        unique=True,
    )
    slug = SlugField(
        verbose_name='Slug для тега',
        max_length=200,
        unique=True,
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ('name',)


class Recipe(Model):
    author = ForeignKey(
        to=User,
        on_delete=CASCADE,
        verbose_name='Автор рецепта',
        related_name='recipes'
    )
    cooking_time = PositiveIntegerField(
        verbose_name='Время приготовления',
        validators=(
            MinValueValidator(1, 'Значение не может быть менее 1 минуты.'),
        )
    )
    favorite = ManyToManyField(
        to=User,
        verbose_name='Избранные рецепты',
        related_name='favorites'
    )
    ingredients = ManyToManyField(
        to=Ingredient,
        through=IngredientAmount,
        verbose_name='Список ингредиентов',
        related_name='recipes'
    )
    image = ImageField(
        verbose_name='Изображение',
        upload_to='recipe_images/'
    )
    name = CharField(
        verbose_name='Название рецепта',
        max_length=200
    )
    pub_date = DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )
    shopping_cart = ManyToManyField(
        to=User,
        verbose_name='Список покупок',
        related_name='in_cart'
    )
    tags = ManyToManyField(
        to=Tag,
        related_name='recipes',
        verbose_name='Теги'
    )
    text = TextField(
        verbose_name='Описание рецепта',
    )

    def _get_count_added_to_favorite(self):
        return self.favorite.count()

    _get_count_added_to_favorite.short_description = ('Добавлено в избранное'
                                                      ', раз')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ('-pub_date',)
        constraints = (
            UniqueConstraint(
                name='unique_per_author',
                fields=('name', 'author')
            ),
        )
