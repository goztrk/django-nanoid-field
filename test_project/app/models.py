from django.db import models

from nanoid_field import NanoidField


class Test(models.Model):
    id = NanoidField(primary_key=True, editable=False)
    override = NanoidField(alphabet="123456789", max_length=2)
