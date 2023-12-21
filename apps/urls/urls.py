from django.urls import path

from .views import ShortenURLView, MostVisitedUrlsListView, RedirectUrlView

urlpatterns = [
    path('list/', MostVisitedUrlsListView.as_view(), name='most_visited_urls_list'),
    path('shorten/', ShortenURLView.as_view(), name='shorten_url'),
    path('<str:base62_id>/', RedirectUrlView.as_view(), name='redirect_url'),
]