from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.urls.utils import decimal_to_base62
from django_project import settings

from .tasks import get_html_title


class URLs(models.Model):
    base62_id = models.CharField(null=True, unique=True)
    title = models.TextField(null=True, blank=True)
    long_url = models.URLField(unique=True)
    counter = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def short_url(self):
        result = f"{settings.BASE_URL}/{self.base62_id}"
        return result

    def __str__(self):
        return self.long_url

    class Meta:
        verbose_name = 'URL'
        verbose_name_plural = 'URLs'

@receiver(post_save, sender=URLs)
def generate_base62_id(sender, instance, created, **kwargs):
    if not instance.base62_id:
        instance.base62_id = decimal_to_base62(instance.id)
        instance.save()
    
@receiver(post_save, sender=URLs)
def create_url_signal(sender, instance, created, **kwargs):
    if created:
        result = get_html_title.delay(instance.long_url)
        instance.title = result.get()
        instance.save()