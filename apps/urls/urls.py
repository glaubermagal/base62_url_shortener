from django.urls import path

from .views import ShortenURLView, MostVisitedUrlsListView, RedirectUrlView

urlpatterns = [
    path('list/', MostVisitedUrlsListView.as_view(), name='top-100-urls'),
    path('shorten/', ShortenURLView.as_view(), name='shorten-url'),
    path('<str:base62_id>/', RedirectUrlView.as_view(), name='urls-by-base62-id'),
]