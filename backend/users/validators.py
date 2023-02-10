from re import match

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class MinLengthRegValidator:
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
