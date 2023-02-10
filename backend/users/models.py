from re import match

from django.contrib.auth.models import AbstractUser
from django.db.models import (CharField, EmailField,
                              ManyToManyField)
from django.db.models.functions import Length
from django.utils.translation import gettext_lazy

from django.core.exceptions import ValidationError

CharField.register_lookup(Length)


class User(AbstractUser):
    email = EmailField(
        verbose_name='Адрес электронной почты',
        help_text='Обязательное поле',
        unique=True,
        max_length=254
    )
    username = CharField(
        verbose_name='Логин',
        help_text='Обязательное поле',
        unique=True,
        max_length=150,
    )
    first_name = CharField(
        verbose_name='Имя',
        help_text='Обязательное поле',
        max_length=150
    )
    last_name = CharField(
        verbose_name='Фамилия',
        help_text='Обязательное поле',
        max_length=150
    )
    password = CharField(
        verbose_name=gettext_lazy('Пароль'),
        help_text='Обязательное поле',
        max_length=150,
        validators=(
        )
    )
    subscription = ManyToManyField(
        verbose_name='Подписка',
        related_name='Подписчики',
        to='self',
        symmetrical=False
    )

    def validate_username(self, username: str):
        if len(username) < 3:
            raise ValidationError(
                'Длина username допустима от 3 до 150'
            )
        if not match(pattern=r'^[\w.@+-]+$', string=username):
            raise ValidationError(
                'В username допустимы только буквенные символы.'
            )
        return username.lower()

    def validate_password(self, attr):
        super().validate(attr)
        if len(attr.get('password')) >= 150:
            raise ValidationError({
                'password': ('Пароль не может содержать более 150 символов.')
            })
        return attr

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username', 'email')

    def __str__(self) -> str:
        return self.username
