from rest_framework import routers

from movies_app.views.director import DirectorViewSet
from movies_app.views.movie import MovieViewSet


router = routers.SimpleRouter()
router.register(r'director', DirectorViewSet)
router.register(r'movies', MovieViewSet)
urlpatterns = router.urls
