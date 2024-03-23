import factory
import pytest

from movies_app.models import Director


@pytest.fixture()
def director_factory():
    class DirectorFactory(factory.django.DjangoModelFactory):
        class Meta:
            model = Director

        fio = factory.Faker('name')

    return DirectorFactory
