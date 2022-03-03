# Generated by Django 4.0.1 on 2022-02-27 13:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0009_remove_country_data_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country_data',
            name='liked',
            field=models.ManyToManyField(blank=True, default=None, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='country_data',
            name='population',
            field=models.IntegerField(),
        ),
    ]