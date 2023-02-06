from string import hexdigits

from rest_framework.serializers import ValidationError


def class_obj_validate(value: str, klass: object = None) -> object:
    if not str(value).isdecimal():
        raise ValidationError(
            f'Строка {value} должна содержать число.'
        )
    if klass:
        obj = klass.objects.filter(id=value)
        if not obj:
            raise ValidationError(
                f'Обекта {type(klass)} с ID={value} не существует.'
            )
        return obj[0]
    return None


def hex_color_validate(value: str) -> None:
    if len(value) not in (3, 6):
        raise ValidationError(
            f'Длинна {value} не кратна 3.'
        )
    if not set(value).issubset(hexdigits):
        raise ValidationError(
            f'{value} не шестнадцатиричное.'
        )
