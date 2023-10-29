from django.conf import settings
from django.db import models

from nanoid import generate


DEFAULT_ALPHABET = (
    "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz-"  # noqa: 501
)
DEFAULT_SIZE = 21


class NanoidField(models.CharField):
    def __init__(self, *args, **kwargs) -> None:
        self.alphabet = kwargs.pop(
            "alphabet", getattr(settings, "NANOID_ALPHABET", DEFAULT_ALPHABET)
        )
        kwargs["max_length"] = kwargs.pop("max_length", DEFAULT_SIZE)
        kwargs["default"] = self.nanoid

        super(NanoidField, self).__init__(*args, **kwargs)

    def nanoid(self):
        return generate(self.alphabet, self.max_length)
