from django.urls import path
from rest_framework import routers
from catalog import views
from rest_framework.renderers import JSONOpenAPIRenderer

from rest_framework.schemas import get_schema_view


router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'genres', views.GenreViewSet)
router.register(r'languages', views.LanguageViewSet)
router.register(r'authors', views.AuthorViewSet)

urlpatterns = [
    # ...
    # Use the `get_schema_view()` helper to add a `SchemaView` to project URLs.
    #   * `title` and `description` parameters are passed to `SchemaGenerator`.
    #   * Provide view name for use with `reverse()`.
    path('openapi.yaml', get_schema_view(
        title="Your Project",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi-schema-yaml'),
    path('openapi.json', get_schema_view(
            title="Your Project",
            version="1.0.0",
            renderer_classes = [JSONOpenAPIRenderer],
        ), name='openapi-schema-json'),
]
