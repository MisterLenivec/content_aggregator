# Generated by Django 3.1.3 on 2020-12-28 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image_url',
            field=models.URLField(blank=True, max_length=350, verbose_name='Image link'),
        ),
    ]
