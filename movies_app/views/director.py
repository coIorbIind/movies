from rest_framework.viewsets import ModelViewSet


from movies_app.models import Director
from movies_app.serializers import DirectorSerializer


class DirectorViewSet(ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
