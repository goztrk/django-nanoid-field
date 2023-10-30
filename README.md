# Django NanoID Field

NanoID is an alternative to UUID, CUID for generating random IDs. This package
provides a field to use in models.


## Installation

Install it from PyPI:

```sh
pip install django-nanoid-field
```


## Usage

First, add it to your applications (Not Required)

```python
INSTALLED_APPS = [
    # ...
    'nanoid_field',
    # ...
]
```

You can now use it in your models like:

```python
from django.db import models
from nanoid_field import NanoidField

class Profile(models.Model):
    hash = NanoidField(max_length=10, alphabet='0123456789abcdefghijklmnopqrstuvwxyz)
```


## NanoidField

This model field is based on `CharField`. All of it's parameters can be used.

Additionally following fields affects outcome of NanoID:


### `max_length` Parameter (Optional)
Determines size of the generated ID as well as length of the field in Database.

#### **DEFAULT:**
```
21
```


### `alphabet` Parameter (Optional)
This optional parameter helps you to determine which characters will be used to
build up.

#### **DEFAULT:**
```
0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz-
```


## Using NanoidField as `primary_key`

Currently Django Auto Field feature does not allow using fields other than
Integer based fields. Until this ability changes you cannot use this as AutoField.

To use NanoID as default `primary_key` you need to explicitly define it in your
model:

```python
from django.db import models


class SomeModel(models.Model):
    id = NanoidField()
    # ...
```

## Changing defaults
`django-nanoid-field` also provides two settings to change defaults of `alphabet`
and `max_length`. You can change those by adding them to your `settings.py` file

```python
# settings.py file

NANOID_ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz-"
NANOID_SIZE = 21
```
