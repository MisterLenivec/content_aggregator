from django.urls import path, include
from rest_framework import routers

from .views import ArticleViewSet, SiteBoardViewSet, CategoryViewSet


router = routers.DefaultRouter()
router.register('articles', ArticleViewSet)
router.register('boards', SiteBoardViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = [
#     path('articles/', ArticleViewSet.as_view({'get': 'list'})),
#     path('articles/<int:pk>/', ArticleViewSet.as_view({'get': 'retrieve'})),
#     path('boards/', SiteBoardViewSet.as_view({'get': 'list'})),
#     path('boards/<int:pk>/', SiteBoardViewSet.as_view({'get': 'retrieve'})),
#     path('categories/', CategoryViewSet.as_view({'get': 'list'})),
#     path('categories/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve'})),
# ]
