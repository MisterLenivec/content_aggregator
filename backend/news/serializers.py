from rest_framework.serializers import ModelSerializer, SlugRelatedField

from .models import SiteBoard, Article, Category


class ArticleSerializer(ModelSerializer):
    """Article serializer"""
    site_board = SlugRelatedField(slug_field='site_name', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class SiteBoardSerializer(ModelSerializer):
    """Website board serializer"""
    category = SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = SiteBoard
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    """Category serializer"""

    class Meta:
        model = Category
        fields = '__all__'
