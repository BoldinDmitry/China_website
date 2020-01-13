from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import Internship
from .serializers import InternshipSerializer


class InternshipView(viewsets.ReadOnlyModelViewSet):
    serializer_class = InternshipSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "id",
        "name",
        "time",
        "place",
        "city",
        "organization",
        "conditions",
        "rating",
        "description",
        "start",
        "end",
    ]

    def get_queryset(self):
        return Internship.objects.all().filter(is_active=True).order_by("start")
