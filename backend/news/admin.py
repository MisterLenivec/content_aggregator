from django.contrib import admin

from .models import Category, SiteBoard, Article


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category on admin panel"""
    list_display = ('id', 'name', 'slug')
    list_display_links = ('name',)
    readonly_fields = ('id',)


@admin.register(SiteBoard)
class SiteBoardAdmin(admin.ModelAdmin):
    """Website board on admin panel"""
    list_display = ('id', 'site_name', 'url', 'category')
    list_display_links = ('site_name',)
    list_filter = ('category',)
    readonly_fields = ('id',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """Article on admin panel"""
    list_display = ('id', 'get_short_title', 'created_at', 'site_board')
    list_display_links = ('get_short_title',)
    list_filter = ('site_board', 'created_at')
    readonly_fields = ('created_at', 'id')

    def get_short_title(self, obj):
        return f'{obj.title[:47]}...' if len(obj.title) > 50 else obj.title

    get_short_title.short_description = 'title'
