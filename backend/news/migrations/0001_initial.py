# Generated by Django 3.1.2 on 2020-10-28 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Category')),
                ('description', models.TextField(max_length=200, verbose_name='Description')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='SiteBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=100, verbose_name='Name of the site')),
                ('description', models.TextField(blank=True, max_length=200, verbose_name='Description')),
                ('url', models.URLField(unique=True, verbose_name='Link')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Site board',
                'verbose_name_plural': 'Site boards',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('description', models.TextField(max_length=350, verbose_name='Description')),
                ('url', models.URLField(unique=True, verbose_name='Link')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('site_board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.siteboard', verbose_name='Site board')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
