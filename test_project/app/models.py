from django.db import models

from nanoid_field import NanoidField


class Test(models.Model):
    id = NanoidField()
    override = NanoidField(
        alphabet="123456789",
        size=2,
        primary_key=False,
        editable=True
    )
