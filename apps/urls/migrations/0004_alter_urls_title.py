# Generated by Django 5.0 on 2023-12-21 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urls', '0003_urls_counter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='title',
            field=models.TextField(null=True),
        ),
    ]
