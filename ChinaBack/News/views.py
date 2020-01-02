from .serializers import NewsSerializer
from .models import News

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from django.utils import timezone


class NewsView(viewsets.ReadOnlyModelViewSet):
    serializer_class = NewsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'id',
        'title',
        'publication_date',
        'short_text',
        'text',
        'tag'
    ]

    def get_queryset(self):
        return News.objects.filter(publication_date__lte=timezone.now()).order_by("publication_date")
