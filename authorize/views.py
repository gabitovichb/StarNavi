from django.shortcuts import render
from rest_framework.views import *
from rest_framework.response import *

class Index(APIView):
    def get(self, request):
        return Response({'result':'Hello World'})

