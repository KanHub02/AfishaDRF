from django.db import models
from django.db.models import Sum

RATING = [
    (1, "*"),
    (2, "**"),
    (3, "***"),
    (4, "****"),
    (5, "*****"),
]


class Genre(models.Model):
    ganre = models.CharField(max_length=100)

    def __str__(self):
        return self.ganre


class Tag(models.Model):
    htag = models.CharField(max_length=100)

    def __str__(self):
        return self.htag


class Director(models.Model):
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, null=True)
    age = models.PositiveIntegerField(null=True, blank=True)




    def __str__(self):
        return self.name


class Movie(models.Model):
    ganre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)
    tag = models.ManyToManyField(Tag, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    duration = models.PositiveIntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    @property
    def tag_list(self):
        return [i.htag for i in self.tag.all()]


class Review(models.Model):
    stars = models.IntegerField(choices=RATING, default=5, null=True)
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="review",null=True)

    def __str__(self):
        return self.text

    @property
    def rating(self):
        s = Review.objects.all().aggregate(Sum("stars"))["stars__sum"]
        c = Review.objects.all().count()
        try:
            return s / c
        except:
            return 0
