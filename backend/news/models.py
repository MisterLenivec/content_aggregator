from django.db import models


class Category(models.Model):
    """Site category"""
    name = models.CharField('Category', max_length=50, unique=True)
    description = models.TextField('Description', max_length=200)
    slug = models.SlugField('Slug', max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class SiteBoard(models.Model):
    """Website board"""
    site_name = models.CharField('Name of the site', max_length=100)
    description = models.TextField('Description', max_length=200, blank=True)
    url = models.URLField('Link', unique=True)
    image_url = models.URLField('Image link', blank=True, max_length=350)
    category = models.ForeignKey(
        Category, verbose_name='Category', related_name='boards',
        on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = 'Site board'
        verbose_name_plural = 'Site boards'
        ordering = ['-id']


class Article(models.Model):
    """Article on the board"""
    title = models.CharField('Title', max_length=200)
    description = models.TextField('Description', max_length=350)
    url = models.URLField('Link', unique=True)
    image_url = models.URLField('Image link', blank=True, max_length=350)
    created_at = models.DateTimeField('Created date', auto_now_add=True)
    site_board = models.ForeignKey(
        SiteBoard, verbose_name='Site board',
        related_name='articles', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
