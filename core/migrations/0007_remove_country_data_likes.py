# Generated by Django 4.0.1 on 2022-02-24 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_country_data_likes_alter_country_data_population'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country_data',
            name='likes',
        ),
    ]