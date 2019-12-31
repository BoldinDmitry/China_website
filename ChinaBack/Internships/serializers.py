from .models import Internship

from rest_framework import serializers


class InternshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internship
        exclude = ('is_active', )
