from django.contrib.auth.models import AbstractUser
from django.db.models import (CharField, EmailField,
                              ManyToManyField)
from django.db.models.functions import Length


CharField.register_lookup(Length)


class User(AbstractUser):
    email = EmailField(
        'Электронная почта',
        max_length=254,
        unique=True
    )
    first_name = CharField(
        'Имя',
        max_length=150,
        blank=False
    )
    last_name = CharField(
        'Фамилия',
        max_length=150,
        blank=False
    )
    username = CharField(
        'Уникальное имя',
        max_length=150,
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    subscription = ManyToManyField(
        verbose_name='Подписка',
        related_name='followers',
        to='self',
        symmetrical=False
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('-pk', )

    def __str__(self) -> str:
        return self.username
