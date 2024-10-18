from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name", "full_name"]

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ["id", "name", "rows", "seats_in_row", "capacity"]


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)
    actors = serializers.ListField(child=serializers.PrimaryKeyRelatedField(queryset=Actor.objects.all()), required=False)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'duration', 'genres', 'actors']

    def validate(self, attrs):
        # Add custom validation logic here if needed
        if 'actors' in attrs:
            if not attrs['actors']:
                raise ValidationError('At least one actor must be specified.')
        return attrs


class MovieSessionSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(
        source="movie.title",
        read_only=True)
    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name",
        read_only=True)
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity",
        read_only=True)

    class Meta:
        model = MovieSession
        fields = ["id",
                  "show_time",
                  "movie_title",
                  "cinema_hall_name",
                  "cinema_hall_capacity"]
