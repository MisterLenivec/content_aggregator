from rest_framework.serializers import ModelSerializer, SlugRelatedField, HyperlinkedRelatedField

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
    articles = ArticleSerializer(many=True, read_only=True)
    # articles = HyperlinkedRelatedField(many=True, read_only=True,
    #                                    view_name='article-detail')

    class Meta:
        model = SiteBoard
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    """Category serializer"""
    # boards = SiteBoardSerializer(many=True, read_only=True)
    boards = HyperlinkedRelatedField(many=True, read_only=True,
                                       view_name='siteboard-detail')

    class Meta:
        model = Category
        fields = '__all__'
