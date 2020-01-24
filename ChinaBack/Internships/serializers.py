from rest_framework import serializers

from .models import Internship


class InternshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internship
        exclude = ("is_active",)

    def get_image1(self, image):
        return self.get_image_path(image)

    def get_image2(self, image):
        return self.get_image_path(image)

    def get_image3(self, image):
        return self.get_image_path(image)

    def get_image4(self, image):
        return self.get_image_path(image)

    def get_image_path(self, image):
        request = self.context.get('request')
        photo_url = image.url
        return request.build_absolute_uri(photo_url)

