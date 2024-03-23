from rest_framework import serializers

from movies_app.models import Movie
from .director import DirectorSerializer


class MovieCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def to_representation(self, obj):
        if self.context['request'].method == 'GET':
            serializer = MovieGetSerializer(obj)
            return serializer.data
        return super().to_representation(obj)


class MovieShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    length = serializers.SerializerMethodField()

    def get_length(self, obj: Movie):
        hours = obj.length // 3600
        minutes = (obj.length - hours * 3600) // 60
        seconds = obj.length - hours * 3600 - minutes * 60
        return (
            f'{"" if hours > 9 else "0"}{hours}:'
            f'{"" if minutes > 9 else "0"}{minutes}:'
            f'{"" if seconds > 9 else "0"}{seconds}'
        )


class MovieGetSerializer(MovieShortSerializer):
    director = DirectorSerializer()
