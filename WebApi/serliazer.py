from rest_framework import serializers
from cv.models import Cv

class CvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cv
        fields = ['name','surname','email','telefon']