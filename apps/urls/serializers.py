from rest_framework import serializers
from .models import URLs

class URLsSerializer(serializers.ModelSerializer):
    class Meta:
        model = URLs
        fields = ('long_url', 'short_url', 'title')
        # exclude = ('id',)