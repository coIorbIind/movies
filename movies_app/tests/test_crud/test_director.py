import pytest

from movies_app.models import Director


@pytest.mark.django_db
def test_get_directors(client, director_factory):
    director1 = director_factory()
    director2 = director_factory()
    response = client.get('/api/director/')
    assert response.status_code == 200
    assert {item['id'] for item in response.json()} == {director1.id, director2.id}


@pytest.mark.django_db
@pytest.mark.parametrize('correct', [True, False])
def test_get_director(client, director_factory, correct):
    director = director_factory()

    if correct:
        director_id = director.id
        status_code = 200
    else:
        director_id = 0
        status_code = 404

    response = client.get(f'/api/director/{director_id}/')
    assert response.status_code == status_code


@pytest.mark.django_db
@pytest.mark.parametrize('correct', [True, False])
def test_delete_director(client, director_factory, correct):
    director = director_factory()

    if correct:
        director_id = director.id
        status_code = 204
    else:
        director_id = 0
        status_code = 404

    response = client.delete(f'/api/director/{director_id}/')
    assert response.status_code == status_code


@pytest.mark.django_db
def test_create_director(client):
    fio = 'Иванов Иван Иванович'
    response = client.post(f'/api/director/', data={'fio': fio})
    assert response.status_code == 201

    data = response.json()
    director = Director.objects.get(pk=data['id'])
    assert director.fio == fio


@pytest.mark.django_db
@pytest.mark.parametrize('correct', [True, False])
def test_update_director(client, director_factory, correct):
    director = director_factory()
    new_fio = 'Иванов Иван Иванович'

    if correct:
        director_id = director.id
        status_code = 200
    else:
        director_id = 0
        status_code = 404

    response = client.patch(f'/api/director/{director_id}/', data={'fio': new_fio}, content_type='application/json')
    assert response.status_code == status_code

    if correct:
        director.refresh_from_db()
        assert director.fio == new_fio
