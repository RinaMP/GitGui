from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from.models import student
from.models import subjects
from .serializer import wappseriazer
from .serializer import subjectsseriazer

class studentViewSet (ModelViewSet):
    serializer_class = wappseriazer
    queryset = student.objects.all()


class subjectsViewSet (ModelViewSet):
    serializer_class = subjectsseriazer
    queryset = subjects.objects.all()


