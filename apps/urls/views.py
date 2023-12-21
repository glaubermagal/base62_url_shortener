from urllib.parse import urlparse

from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import RedirectView
from rest_framework import generics, status
from rest_framework.response import Response

from .models import URLs
from .serializers import URLsSerializer


class RedirectUrlView(RedirectView):
    permanent = True

    def get_redirect_url(self, *args, **kwargs):
        base62_id = self.kwargs.get('base62_id')
        url = URLs.objects.filter(base62_id=base62_id).first()

        if url:
            url.counter += 1
            url.save()
            return url.long_url
        
        raise Http404("Not Found")

class MostVisitedUrlsListView(generics.ListAPIView):
    serializer_class = URLsSerializer

    def get_queryset(self):
        queryset = URLs.objects.all().order_by('-counter')[:100]
        return queryset

class ShortenURLView(generics.CreateAPIView):
    serializer_class = URLsSerializer

    def is_valid_url(self, url):
        parsed_url = urlparse(url)
        return parsed_url.scheme and parsed_url.netloc

    def get(self, request, *args, **kwargs):
        long_url = self.request.query_params.get('url')

        if not long_url:
            return Response({'error': 'url parameter is required in the query parameters.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not self.is_valid_url(long_url):
            return Response({'error': 'url is invalid.'}, status=status.HTTP_400_BAD_REQUEST)

        existing_url = URLs.objects.filter(long_url=long_url).first()

        if existing_url:
            response_data = {
                'short_url': existing_url.short_url
            }
            return Response(response_data, status=status.HTTP_200_OK)

        serializer = self.get_serializer(data={'long_url': long_url})

        if serializer.is_valid():
            new_instance = serializer.save()
            response_data = {
                'short_url': new_instance.short_url
            }
            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

