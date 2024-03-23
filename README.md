## Проект по работе с фильмами

### Запуск
1. Скачайте репозиторий `git clone https://github.com/coIorbIind/movies.git`
2. При необходимости установите необходимые переменные окружения в файле `.env.template`
3. Переименуйте файл `.env.template` в `.env`
4. Для запуска приложения выполните команду `docker compose up --build`
5. При необходимости создания суперпользователя воспользуйтесь командой
`docker exec -it movies-app python manage.py createsuperuser`

_После выполнения данных шагов приложение запустится по адресу_ `http://127.0.0.1:8000/`


### Доступный функционал
1. GET `/api/movies` - список всех кинофильмов

```
    [
        {
            "id": 1,
            "title": "Example movie",
            "year": 2018,
            "director": director,
            "length": "02:30:00",
            "rating": 8
        },
    ...
    ]
```

2. GET `/api/movies/:id` - информация о кинофильме с указанным id

необходимо возвратить ответ с кодом 200 (OK) и вложить JSON следующей структуры:

```
    {
        "id": 1,
        "title": "Example movie",
        "year": 2018,
        "director": director,
        "length": "02:30:00",
        "rating": 8
    }
```

3. POST `/api/movies` - добавление новой записи о кинофильме

В теле входящего запроса необходимо ожидать JSON следующей структуры:
```
    {
        "title": "Example movie",
        "year": 2018,
        "director": director,
        "length": "02:30:00",
        "rating": 8
    }
```
В теле ответа необходимо ожидать JSON следующей структуры:
```
    {
        "id": 1,
        "title": "Example movie",
        "year": 2018,
        "director": director,
        "length": "02:30:00",
        "rating": 8
    }
```

4. PATCH `/api/movies/:id` - изменение информации о кинофильме с указанным id

5. DELETE `/api/movies/:id` - удаление записи с указанным id

