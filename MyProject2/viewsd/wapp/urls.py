from rest_framework.routers import DefaultRouter
from.views import studentViewSet
from.views import subjectsViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('student',studentViewSet)
router.register('subject',subjectsViewSet)


urlpatterns= [
    path ( 'api/',include(router.urls)),
]
