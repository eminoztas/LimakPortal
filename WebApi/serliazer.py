from rest_framework import serializers
from cv.models import Cv

class CvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cv
        fields =['ID','FirstName','LastName', 'DateOfBirth', 'cvImage','EducationalLevel','Summary','Tel','Adress','email']
