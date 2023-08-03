"""Валидаторы для приложения computers."""

from django.core import validators
from django.utils.translation import gettext_lazy as _

KEY_FORMAT_REGEXP: str = r'[\d\w]{5}-[\d\w]{5}-[\d\w]{5}-[\d\w]{5}-[\d\w]{5}'

validate_key = validators.RegexValidator(
    regex=KEY_FORMAT_REGEXP,
    message=_('invalid key format'),
)
