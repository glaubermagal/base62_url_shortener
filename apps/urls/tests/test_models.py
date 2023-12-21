from django.test import TestCase
from apps.urls.models import URLs
from django_project import settings

class URLsModelTest(TestCase):

    def test_create_url(self):
        url = URLs.objects.create(
            id=12345,
            long_url='https://www.google.com/',
        )

        self.assertEqual(url.base62_id, '3D7')
        self.assertEqual(url.title, None)

    def test_get_short_url(self):
        url = URLs.objects.create(
            id=987654321,
            long_url='https://www.google.com/'
        )

        self.assertEqual(url.short_url, f'{settings.BASE_URL}/14q60P')
