from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import Author, Heading
from .serializers import AuthorSerializer, HeadingSerializer


class HeadingsView(viewsets.ReadOnlyModelViewSet):
    serializer_class = HeadingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "id",
        "title",
        "publication_date",
        "short_text",
        "text",
        "author",
    ]

    def get_queryset(self):
        return Heading.objects.all().order_by("publication_date")


class AuthorView(viewsets.ReadOnlyModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "id",
        "name",
        "description",
    ]
