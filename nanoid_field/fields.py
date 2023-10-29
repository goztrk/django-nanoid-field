from typing import Any

from django.conf import settings
from django.db import models

from nanoid import generate


DEFAULT_ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz-"  # noqa: 501
DEFAULT_SIZE = 21


class NanoidField(models.CharField):
    def __init__(
        self,
        alphabet: str = None,
        size: int = None,
        *args: Any,
        **kwargs: Any
    ) -> None:
        default_alphabet = settings.get('NANOID_ALPHABET', DEFAULT_ALPHABET)
        default_size = settings.get('NANOID_SIZE', DEFAULT_SIZE)
        default_primary_key = settings.get('NANOID_PRIMARY_KEY', True)
        default_editable = settings.get('NANOID_EDITABLE', False)

        self.alphabet = alphabet if alphabet else default_alphabet
        self.size = size if size else default_size

        kwargs['primary_key'] = kwargs.pop('primary_key', default_primary_key)
        kwargs['editable'] = kwargs.pop('editable', default_editable)
        kwargs['max_length'] = self.size
        kwargs['default'] = self.nanoid

        super(NanoidField, self).__init__(*args, **kwargs)

    def nanoid(self):
        return generate(self.alphabet, self.size)
