from django.contrib import admin

from .models import URLs

class URLsAdmin(admin.ModelAdmin):
    list_display = ('long_url', 'short_url')
    exclude = ('base62_id',)

admin.site.register(URLs, URLsAdmin)