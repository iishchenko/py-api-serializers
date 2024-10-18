from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cinema.views import GenreViewSet, ActorViewSet, CinemaHallViewSet, MovieViewSet, MovieSessionViewSet

router = DefaultRouter()
router.register(r'genres', GenreViewSet)
router.register(r'actors', ActorViewSet)
router.register(r'cinema_halls', CinemaHallViewSet)
router.register(r'movies', MovieViewSet)
router.register(r'movie_sessions', MovieSessionViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Ensure this is included correctly
]

