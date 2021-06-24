from django.urls import path
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from django.conf.urls import include
from api.views import MovieViewSet, RatingViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'ratings', RatingViewSet)
urlpatterns = [
    path('', include(router.urls))
]
