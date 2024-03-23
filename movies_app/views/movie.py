from rest_framework.viewsets import ModelViewSet


from movies_app.models import Movie
from movies_app.serializers import MovieShortSerializer, MovieGetSerializer, MovieCreateSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method != 'GET':
            return MovieCreateSerializer
        if self.action == 'list':
            return MovieShortSerializer
        if self.action == 'retrieve':
            return MovieGetSerializer
        return MovieShortSerializer
