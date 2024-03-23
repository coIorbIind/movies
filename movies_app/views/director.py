from rest_framework.viewsets import ModelViewSet


from movies_app.models import Director
from movies_app.serializers import DirectorSerializer, DirectorCreateSerializer


class DirectorViewSet(ModelViewSet):
    queryset = Director.objects.all()

    def get_serializer_class(self):
        if self.request.method != 'GET':
            return DirectorCreateSerializer
        return DirectorSerializer
