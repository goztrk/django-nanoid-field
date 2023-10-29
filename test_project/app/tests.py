from django.test import TestCase
from test_project.app.models import Test


class NanoidFieldTest(TestCase):
    def test_simple(self):
        t1 = Test.objects.create()
        self.assertEqual(21, len(t1.id))
        self.assertEqual(2, len(t1.override))

        t2 = Test.objects.create()
        self.assertNotEqual(t1.id, t2.id)
        self.assertNotEqual(t1.override, t2.override)

        self.assertRegex(t1.override, "[0-9]{2}")
        self.assertRegex(t2.override, "[0-9]{2}")
