from .serializers import InternshipSerializer
from .models import Internship

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets


class InternshipView(viewsets.ReadOnlyModelViewSet):
    serializer_class = InternshipSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'id',
        'name',
        'time',
        'place',
        'conditions',
        'rating',
        'start',
        'end'
    ]

    def get_queryset(self):
        return Internship.objects.all().filter(is_active=True).order_by('start')
