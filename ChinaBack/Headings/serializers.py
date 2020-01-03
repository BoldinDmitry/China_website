from rest_framework import serializers

from .models import Author, Heading


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class HeadingSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Heading
        fields = "__all__"
