"""Валидаторы для приложения computers."""

from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

KEY_FORMAT_REGEXP: str = r'[\d\w]{5}-[\d\w]{5}-[\d\w]{5}-[\d\w]{5}-[\d\w]{5}'

validate_office_key = validators.RegexValidator(
    regex=KEY_FORMAT_REGEXP,
    message=_('invalid key format'),
)

validate_os_key = validators.RegexValidator(
    regex=KEY_FORMAT_REGEXP,
    message=_('invalid key format'),
)

def validate_os_bit_depth(value: int) -> None:
    """Проверка разрядности ОС."""
    if value not in (32, 64):
        raise ValidationError(_('invalid os bit length'))
