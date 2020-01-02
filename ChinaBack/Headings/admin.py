from django.contrib import admin

from .models import Author, Heading, Image

admin.site.register(Author)
admin.site.register(Heading)
admin.site.register(Image)
