
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Director, Movie, Review, Genre, Tag
from rest_framework import serializers


class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = "id name ".split()

class DirectorDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = "__all__"


class ReviweSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "id text movie stars rating ".split()


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "id ganre".split()


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "id htag".split()


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "id title ".split()


class MovieDetailSerializer(serializers.ModelSerializer):
    ganre = GenreSerializer()
    tag = TagSerializer(many=True)
    review = ReviweSerializer(many=True)

    class Meta:
        model = Movie
        fields = "id title ganre tag tag_list review".split()



class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30, min_length=5)

    def velidate_director_id(self, director_id):
        if Director.objects.filter(id=director_id).count() == 0:
            raise ValidationError(f"Director with id={director_id} not found!")
        return director_id


class ReviewValidateCreateUpdateSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=30,min_length=3)
    movie = serializers.IntegerField(min_value=1,max_value=1000000,allow_null=True)
    stars = serializers.IntegerField()

    def validate_reviews_id(self, reviews_id):
        if Review.objects.filter(id=reviews_id).count() == 0:
            raise ValidationError(f"Reviews with id={reviews_id} not found!")
        return


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=3)
    description = serializers.CharField()
    duration = serializers.IntegerField()
    director = serializers.IntegerField(allow_null=True)

    def validate_movie_id(self, movie_id):
        if Movie.objects.filter(id=movie_id).count() == 0:
            raise ValidationError(f"Movie with id={movie_id} not found!")
        return movie_id



class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate_username(self,username):
        if User.objects.filter(username=username):
            raise ValidationError('User already exists')
        return username