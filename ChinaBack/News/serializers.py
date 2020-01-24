from rest_framework import serializers

from .models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"

    def get_image(self, news):
        request = self.context.get('request')
        photo_url = news.image.url
        return request.build_absolute_uri(photo_url)
