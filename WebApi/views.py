from django.shortcuts import render
from cv.models import Cv,Personnel
from WebApi.serliazer import CvSerializer
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework import status 

from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions




# Create your views here.




class CvAPIView(APIView):
    @permission_classes((permissions.AllowAny,))
    def get(self, request):
        cv = Cv.objects.all()
        serializer = CvSerializer(cv, many=True)
        return Response(serializer.data)

    @permission_classes((permissions.AllowAny,))
    def post(self, request):
        serializer = CvSerializer(data=request.data)
        import pdb; pdb.set_trace()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        pass

    def delete(self, request):
        pass

        