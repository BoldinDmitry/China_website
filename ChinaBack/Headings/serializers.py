from rest_framework import serializers

from .models import Author, Heading


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

    def get_image(self, news):
        request = self.context.get('request')
        photo_url = news.image.url
        return request.build_absolute_uri(photo_url)


class HeadingSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Heading
        fields = "__all__"
