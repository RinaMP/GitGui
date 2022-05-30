from rest_framework.serializers import ModelSerializer
from .models import student
from .models import subjects

class wappseriazer (ModelSerializer):
    class Meta :
        model = student
        fields = '__all__'


class subjectsseriazer (ModelSerializer):
    class Meta :
        model = subjects
        fields = '__all__'


