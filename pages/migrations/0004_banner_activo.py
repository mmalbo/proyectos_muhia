# Generated by Django 4.2 on 2024-03-06 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]