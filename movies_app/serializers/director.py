from rest_framework import serializers

from movies_app.models import Director


class DirectorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        exclude = ('id', )


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'
