from django.contrib import admin
from .models import Director, Movie, Review, Genre, Tag

admin.site.register(Director)
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Genre)
admin.site.register(Tag)
