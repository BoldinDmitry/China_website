from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Quote
from .serializers import QuoteSerializer

from rest_framework import viewsets


class RandomQuoteView(viewsets.ReadOnlyModelViewSet):
    """
        Lists information related to the current user.
    """
    serializer_class = QuoteSerializer
    permission_classes = (AllowAny,)

    def get_object(self):
        return Quote.objects.order_by("?").first()

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        return Response(serializer.data)
