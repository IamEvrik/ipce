"""Валидаторы для приложения computers."""

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_office_key(value: str) -> None:
    """Проверка ключа офиса."""
    # TODO (evrik): сделать проверку ключа по шаблону


def validate_os_key(value: str) -> None:
    """Проверка кллюча ОС."""
    # TODO (evrik): сделать проверку ключа по шаблону


def validate_os_bit_depth(value: int) -> None:
    """Проверка разрядности ОС."""
    if value not in (32, 64):
        raise ValidationError(_('invalid os bit length'))
