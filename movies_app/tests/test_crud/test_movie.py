import pytest

from movies_app.models import Movie


@pytest.mark.django_db
def test_get_movies(client, movie_factory):
    movie1 = movie_factory()
    movie2 = movie_factory()
    response = client.get('/api/movies/')
    assert response.status_code == 200
    assert {item['id'] for item in response.json()} == {movie1.id, movie2.id}


@pytest.mark.django_db
@pytest.mark.parametrize('correct', [True, False])
def test_get_movie(client, movie_factory, correct):
    movie = movie_factory()

    if correct:
        movie_id = movie.id
        status_code = 200
    else:
        movie_id = 0
        status_code = 404

    response = client.get(f'/api/movies/{movie_id}/')
    assert response.status_code == status_code


@pytest.mark.django_db
@pytest.mark.parametrize('correct', [True, False])
def test_delete_movie(client, movie_factory, correct):
    movie = movie_factory()

    if correct:
        movie_id = movie.id
        status_code = 204
    else:
        movie_id = 0
        status_code = 404

    response = client.delete(f'/api/movies/{movie_id}/')
    assert response.status_code == status_code


@pytest.mark.django_db
def test_create_movie(client, director_factory):
    director = director_factory()
    data = {
        'title': 'title',
        'year': 2000,
        'director': director.id,
        'length': 3600,
        'rating': 10,
    }
    response = client.post(f'/api/movies/', data=data)
    assert response.status_code == 201

    data = response.json()
    movie = Movie.objects.get(pk=data['id'])
    assert movie.title == data['title']
    assert movie.year == data['year']
    assert movie.director_id == data['director']
    assert movie.length == data['length']
    assert movie.rating == data['rating']


@pytest.mark.django_db
@pytest.mark.parametrize('correct', [True, False])
def test_update_movie(client, movie_factory, correct):
    movie = movie_factory()
    new_title = 'new title'

    if correct:
        movie_id = movie.id
        status_code = 200
    else:
        movie_id = 0
        status_code = 404

    response = client.patch(f'/api/movies/{movie_id}/', data={'title': new_title}, content_type='application/json')
    assert response.status_code == status_code

    if correct:
        movie.refresh_from_db()
        assert movie.title == new_title
