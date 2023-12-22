from django.test import TestCase
from apps.urls.models import URLs
from django_project import settings

class URLsModelTest(TestCase):

    def test_create_url(self):
        url_instance = URLs.objects.create(
            id=12345,
            long_url='https://example.com/',
        )
        
        self.assertEqual(url_instance.base62_id, '3D7')

    def test_get_short_url(self):
        url_instance = URLs.objects.create(
            id=987654321,
            long_url='https://example.com/'
        )

        self.assertEqual(url_instance.short_url, f'{settings.BASE_URL}/14q60P')
