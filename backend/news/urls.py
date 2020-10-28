from django.urls import path

from .views import ArticleViewSet, SiteBoardViewSet, CategoryViewSet


urlpatterns = [
    path('article/', ArticleViewSet.as_view({'get': 'list'})),
    path('article/<int:pk>/', ArticleViewSet.as_view({'get': 'retrieve'})),
    path('board/', SiteBoardViewSet.as_view({'get': 'list'})),
    path('board/<int:pk>/', SiteBoardViewSet.as_view({'get': 'retrieve'})),
    path('category/', CategoryViewSet.as_view({'get': 'list'})),
    path('category/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve'})),
]
