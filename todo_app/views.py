from django.http.response import JsonResponse
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from rest_framework import status
from rest_framework.serializers import Serializer


from todo_app.serializers import TodoSerializer

class TodoAPIView(APIView):
    serializer_class = TodoSerializer
    
    
    def get(self,request, pk=None, format=None):
        with open('todos.json') as json_file:
            data = json.load(json_file)
        if pk:
            todo = [item for item in data['items'] if item['id'] == pk]
            return Response({'data': todo})
        return Response({'data': data})