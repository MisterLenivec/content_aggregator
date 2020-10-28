from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import SiteBoard, Article, Category
from .serializers import (
    CategorySerializer,
    SiteBoardSerializer,
    ArticleSerializer
)


class CategoryViewSet(ReadOnlyModelViewSet):
    """Showing categories"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SiteBoardViewSet(ReadOnlyModelViewSet):
    """Displaying site boards"""
    queryset = SiteBoard.objects.all()
    serializer_class = SiteBoardSerializer


class ArticleViewSet(ReadOnlyModelViewSet):
    """Displaying articles"""
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
