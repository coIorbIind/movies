import factory
import pytest

from movies_app.models import Movie


@pytest.fixture()
def movie_factory(director_factory):
    class MovieFactory(factory.django.DjangoModelFactory):
        class Meta:
            model = Movie

        title = factory.Faker('word')
        year = factory.Faker('pyint', min_value=1900, max_value=2100)
        director = factory.SubFactory(director_factory)
        length = factory.Faker('pyint', min_value=3600, max_value=3600 * 10)
        rating = factory.Faker('pyint', min_value=0, max_value=10)

    return MovieFactory
