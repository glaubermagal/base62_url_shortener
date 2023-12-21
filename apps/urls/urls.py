from django.urls import path

from .views import CreateURLView, MostVisitedListView, RedirectUrlView

urlpatterns = [
    path('list/', MostVisitedListView.as_view(), name='top-100-urls'),
    path('create/', CreateURLView.as_view(), name='create-url'),
    path('<str:base62_id>/', RedirectUrlView.as_view(), name='urls-by-base62-id'),
]