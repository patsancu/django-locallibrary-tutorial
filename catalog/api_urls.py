from django.urls import path, include
from rest_framework import routers
from catalog import views


router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'genres', views.GenreViewSet)
router.register(r'languages', views.LanguageViewSet)
router.register(r'authors', views.AuthorViewSet)
