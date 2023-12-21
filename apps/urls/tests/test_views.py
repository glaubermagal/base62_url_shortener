from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from apps.urls.models import URLs


class RedirectUrlViewTest(TestCase):
    def setUp(self):
        self.url = URLs.objects.create(id=17, long_url='http://example.com')

    def test_redirect_url_view(self):
        response = self.client.get(reverse('redirect_url', kwargs={'base62_id': 'H'}))
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)
        self.assertEqual(response.url, 'http://example.com')
        self.assertEqual(URLs.objects.get(base62_id='H').counter, 1)

    def test_redirect_url_view_not_found(self):
        response = self.client.get(reverse('redirect_url', kwargs={'base62_id': 'invalid_id'}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class MostVisitedUrlsListViewTest(TestCase):
    def test_most_visited_urls_list_view(self):
        response = self.client.get(reverse('most_visited_urls_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class ShortenURLViewTest(TestCase):
    def test_shorten_url_view(self):
        url = 'http://example.com'
        response = self.client.get(reverse('shorten_url'), {'url': url})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('short_url', response.data)

    def test_shorten_url_view_existing_url(self):
        url = 'http://example.com'
        response = self.client.get(reverse('shorten_url'), {'url': url})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('short_url', response.data)

    def test_shorten_url_view_invalid_url(self):
        response = self.client.get(reverse('shorten_url'), {'url': 'invalid_url'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)